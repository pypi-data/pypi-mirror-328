from dataclasses import dataclass, field
import random
from typing import Self

from cardnacki.card import Card
from cardnacki.pile import Deck, Pile
from setnacki.logic.models import GameState
from setnacki.logic.play_models import PlayCardModel

RANKS: tuple[str, ...] = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = 'hcds'
SUITS_DICT = {'h': 'hearts', 'c': 'clubs', 'd': 'diamonds', 's': 'spades'}
GAME_POINT_DICT = {'T': 10, 'J': 1, 'Q': 2, 'K': 3, 'A': 4}

# All SetbackMini should be responsible for is playing out hands and returning the outcome;
# don't try to jam in strategies for testing random cards
# can i have an alternate constructor from game state?
# if this blows up, roll it back to the last Git commit
@dataclass
class SetbackMini:
    hands: list[list[str]]
    play_card_models: list[PlayCardModel]
    card_to_lead: str | None = None
    trump: str | None = None  # trump is a single letter: 'hcds'
    player_id: int = 0  # this is Hero
    initial_turn_idx: int = 0  # possible use case: if leader_idx is 1, can test what happens if Hero doesn't bid
    won_piles: list[list[str]] = field(default_factory=lambda: [[], []])
    middle: list[str] = field(default_factory=list)
    deck: list[str] = field(init=False)
    full_deck: Deck = Deck()

    def __post_init__(self):
        # if one player has lead a card, assign initial_turn_idx in case the caller forgot to
        if len(self.hands[0]) != len(self.hands[1]):
            self.initial_turn_idx = 1 if len(self.hands[0]) < len(self.hands[1]) else 0

    @classmethod
    def create_from_game_state(cls, gs: GameState, player_card_models: list[PlayCardModel], player_id: int,
                               card_to_lead: str | None = None) -> Self:
        """Alternate constructor that uses Game State, PCMs, player_id, and card_to_lead"""
        hands = [[c.rank_suit for c in h] for h in gs.grid.hands]
        won_piles = [[c.rank_suit for c in h] for h in gs.grid.won_piles]
        middle = [c.rank_suit for c in gs.grid.middle]
        return cls(hands, player_card_models, card_to_lead, gs.grid.trump[0], player_id, gs.player_turn_idx,
                   won_piles, middle)

    def get_points(self) -> list[int]:
        player_points = [0, 0]
        won_sorted = sorted([(card, i) for i, lst in enumerate(self.won_piles)
                             for card in lst if card[1] == self.trump], key=lambda x: RANKS.index(x[0][0]))
        player_points[won_sorted[-1][1]] += 1  # high
        player_points[won_sorted[0][1]] += 1  # low
        if jack_tuple := (next((c for c in won_sorted if c[0][0] == 'J'), None)):
            player_points[jack_tuple[1]] += 1
        game_points = [sum([GAME_POINT_DICT.get(c[0], 0) for c in pile]) for pile in self.won_piles]
        game_player_idx = 0 if game_points[0] > game_points[1] else 1 if game_points[0] < game_points[1] else None
        if game_player_idx is not None:
            player_points[game_player_idx] += 1
        return player_points

    @property
    def net_points(self) -> int:
        """Returns net points (points won by caller - point won by caller's opponent).  Caller = self.player_id"""
        points = self.get_points()
        return points[0] - points[1] if self.player_id == 0 else points[1] - points[0]

    @property
    def lead_card(self) -> str | None:
        return self.middle[0] if self.middle else None

    def get_playable_cards(self, hand: list[str]) -> list[str] | None:
        """ If there is no lead card or if you don't have any cards of the lead suit, return all cards.
            If you have at least one card of the lead suit, return all cards of that suit and trump. """
        if not hand:
            return None
        if not self.lead_card or self.lead_card[-1] not in {c[-1] for c in hand}:
            return hand
        return [c for c in hand if c[-1] == self.trump or c[-1] == self.lead_card[-1]]

    def get_winning_card(self) -> str:
        return sorted(self.middle,
                      key=lambda x: (x[-1] == self.trump, x[-1] == self.middle[0][-1], RANKS.index(x[0])))[-1]

    def get_trick_winner(self) -> str:
        return 'leader' if self.get_winning_card() == self.middle[0] else 'follower'

    def get_card_to_play(self, p_idx: int) -> str:
        # this method is the only connection to the outside world
        # if the hand is fresh, assign card_to_lead if not provided in init (may be used by caller for stats)
        if len(self.hands[0]) == 6 and len(self.hands[1]) == 6:
            self.card_to_lead = self.card_to_lead or self.hands[p_idx][0]
            self.trump = self.trump or self.card_to_lead[-1]
            return self.card_to_lead

        playable_cards = [self.full_deck[c] for c in self.get_playable_cards(self.hands[p_idx])]

        if len(playable_cards) == 1:
            return playable_cards[0].rank_suit

        lead_card = self.full_deck[self.middle[0]] if self.middle else None
        won_piles = [Pile.create_from_rank_suits(self.full_deck, ' '.join(rs)) for rs in self.won_piles]

        card: Card = self.play_card_models[p_idx].select_card(playable_cards, lead_card,
                                                              SUITS_DICT[self.trump], won_piles, p_idx)
        return card.rank_suit

    def create_opponent_hand(self) -> None:
        if self.hands[1] in ('', None, []):
            self.deck = [f'{r}{s}' for r in RANKS for s in SUITS]
            [self.deck.remove(c) for hand in self.hands for c in hand]
            self.hands[1] = random.sample(self.deck, 6)

    def play(self, sim_cnt: int = 1):
        l = (len(self.middle) + self.initial_turn_idx) % 2  # leader is 0 if len(middle) + initial_player_idx is 0 or 2
        f = 1 if not l else 0  # follower
        self.create_opponent_hand()

        for i in range(sim_cnt):
            while self.hands[0] or self.hands[1]:
                if not self.middle:  # if SetbackMini was created mid-hand, there may already be a lead card
                    leader_card = self.get_card_to_play(l)
                    self.middle.append(leader_card)
                    self.hands[l].remove(leader_card)

                follower_card = self.get_card_to_play(f)
                self.middle.append(follower_card)
                self.hands[f].remove(follower_card)

                winner: str = self.get_trick_winner()
                if winner == 'follower':
                    l, f = f, l
                self.won_piles[l].extend(self.middle)
                self.middle = []
