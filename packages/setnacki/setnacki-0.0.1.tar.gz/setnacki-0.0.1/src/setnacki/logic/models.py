# here, we identify the building blocks of the game
# model domain with Immutable objects, in order to ensure we have:
# modular, composable code that is easier to test/debug/reason

# __future__ must be placed at the very top of the python file
# it allows the forward declaration of GameState in Play
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from enum import StrEnum
from functools import cached_property


from cardnacki.card import Card
from cardnacki.pile import Deck, Pile
from setnacki.logic.validators import (validate_bid, validate_bids,
                                       validate_card_cnt, validate_hand, validate_hands, validate_middle,
                                       validate_play, validate_setback_deck, validate_won_pile, validate_won_piles)

ALL_BIDS = [0, 2, 3, 4]
GAME_UP_TO = 3

@dataclass
class SetbackDeck(Deck):
    def __init__(self):
        super().__init__()
        game_points = {14: 4, 13: 3, 12: 2, 11: 1, 10: 10}
        for c in self.cards:
            c.attributes['game_points'] = game_points.get(c.rank_int, 0)

    def __post_init__(self):
        validate_setback_deck(self)

@dataclass
class CardPile(Pile):
    """Inherits from cardnacki.pile.Pile."""
    cards: list[Card] = field(default_factory=list)

    def __post_init__(self):
        Pile.__init__(self, self.cards)

    @property
    def game_points(self) -> int:
        return sum([c.attributes['game_points'] for c in self.cards])

@dataclass
class Hand(CardPile):
    cards: list[Card] = field(default_factory=list)

    def __post_init__(self):
        Pile.__init__(self, self.cards)
        validate_hand(self)

    def get_playable_cards(self, trump: str = '', ref_card: Card = None) -> list[Card] | None:
        """ If there is no lead card or if you don't have any cards of the lead suit, return all cards.
            If you have at least one card of the lead suit, return all cards of that suit and trump. """
        if not self.cards:
            return None
        if not ref_card or ref_card.suit not in self.pile_props.suits:
            return self.cards
        return [c for c in self.cards if c.suit == trump or c.suit == ref_card.suit]

@dataclass
class WonPile(CardPile):
    cards: list[Card] = field(default_factory=list)

    def __post_init__(self):
        Pile.__init__(self, self.cards)
        validate_won_pile(self)

@dataclass
class Middle(CardPile):
    cards: list[Card] = field(default_factory=list)
    player_indexes: list[int] = field(default_factory=list)

    def __post_init__(self):
        Pile.__init__(self, self.cards)
        validate_middle(self)

    @property
    def lead_card(self) -> Card | None:
        return self.cards[0] if self.cards else None

    def get_winning_card(self, trump: str) -> Card:
        """ Return the highest trump card, else return the highest ranked card of the lead suit """
        if trump_cards := sorted([c for c in self.cards if c.suit == trump], key=lambda x: x.rank_int, reverse=True):
            return trump_cards[0]
        return sorted([c for c in self.cards if c.suit == self.cards[0].suit],
                      key=lambda x: x.rank_int, reverse=True)[0]

    def get_trick_winner_idx(self, trump: str) -> int:
        return next(self.player_indexes[idx] for idx, c in enumerate(self.cards) if c == self.get_winning_card(trump))

class Action(StrEnum):
    BID = 'bid'
    PLAY_CARD = 'play_card'

@dataclass(frozen=True)
class Bid:
    value: int
    player_idx: int

    def __post_init__(self):
        validate_bid(self)

@dataclass(frozen=True)
class Bids:
    bids: list[Bid] = field(default_factory=list)

    @property
    def winning_bid(self) -> Bid | None:
        return next(b for b in self.bids if self._highest_bid_value == b.value) if self.bids else None

    @property
    def winning_bid_int(self) -> int | None:
        """Returns the current highest bid 0, 2, 3, or 4 ... if no bids have yet been lodged, return 0"""
        return next((b.value for b in self.bids if self._highest_bid_value == b.value), 0)

    @property
    def bid_cnt(self) -> int:
        return len(self.bids)

    @property
    def _highest_bid_value(self) -> int | None:
        return max([b.value for b in self.bids]) if self.bids else None


class HandRepresentation:
    @staticmethod
    def create_hand_rep_from_cards(cards: list[Card]) -> tuple[tuple[int, ...]]:
        simple_hand = [HandRepresentation._simplify_card(c) for c in cards]
        all_card_hand_rep = HandRepresentation._generate_hand_rep(simple_hand)
        return HandRepresentation._relevant_suits_two_max(all_card_hand_rep)

    @staticmethod
    def create_cards_from_hand_rep(hand_rep_as_tuple: tuple[tuple[int, ...]], deck: Deck) -> list[Card]:
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        hand_rep_card_cnt = sum([1 for suit in hand_rep_as_tuple for _ in suit])

        hand_rep = list(hand_rep_as_tuple)
        # if the hand representation doesn't have six cards, add in a suit/tuple w a single 8 or 7
        # 8 & 7 are being used as generic middle-of-the-road value cards
        if hand_rep_card_cnt < 6:
            if hand_rep_card_cnt == 5:
                hand_rep.append((8,))
            elif hand_rep_card_cnt == 4:
                hand_rep.append((8, 7))
            elif hand_rep_card_cnt == 3:
                hand_rep.append((8, 7))
                hand_rep.append((8,))
            elif hand_rep_card_cnt == 2:
                hand_rep.append((8, 7))
                hand_rep.append((8, 7))

        return [HandRepresentation._get_card_from_deck(rank_int, suits[idx], deck)
                for idx, suit_group in enumerate(hand_rep) for rank_int in suit_group]

    @staticmethod
    def _get_card_from_deck(rank_int: int, suit: str, deck: Deck) -> Card | None:
        return next((c for c in deck if c.rank_int == rank_int and c.suit == suit), None)

    @staticmethod
    def _simplify_card(c: Card) -> tuple[int, str]:
        """ A compute-saving function to reduce a Card object down to just simply (2, 'h') """
        return c.rank_int, c.suit[0]

    @staticmethod
    def _generate_hand_rep(simple_hand) -> tuple[tuple[int, ...]]:
        """ Convert a simple hand to a two_suit_max reverse-ordered list of tuples e.g. [(14, 10), (12, 3)] """
        # -- group by suit
        grouped_dict = defaultdict(list)
        [grouped_dict[suit].append(rank_int) for rank_int, suit in simple_hand]
        grouped_by_suit = [list(grouped_dict[char]) for char in sorted(grouped_dict)]
        # -- sort
        grouped_by_suit.sort(key=lambda x: [len(x), x[0]], reverse=True)
        [suit.sort(reverse=True) for suit in grouped_by_suit]
        # -- convert suit groups to tuples
        return tuple([tuple(suit) for suit in grouped_by_suit])

    @staticmethod
    def _relevant_suits_two_max(orig_hand_rep: tuple[tuple[int, ...]]) -> tuple[tuple[int, ...]] | None:
        """ A suit must contain either a face card or have three members """
        hand_rep = []
        for suit in orig_hand_rep:
            if len(suit) > 2:
                hand_rep.append(suit)
            else:
                for rank_int in suit:
                    if rank_int >= 10:
                        hand_rep.append(suit)
                        break
            if len(hand_rep) == 2:
                break
        return tuple(hand_rep) if hand_rep else None


@dataclass(frozen=True)
class Grid:
    player_cnt: int
    dealer_idx: int
    hands: list[Hand]
    won_piles: list[WonPile]
    scores: list[int]
    middle: Middle = field(default_factory=Middle)
    bids: Bids = Bids()
    trump: str = None
    prior_trick_winner_idx: int = None
    first_card_of_round: Card = None

    def __post_init__(self):
        validate_card_cnt(self)
        validate_hands(self.hands)
        validate_won_piles(self.player_cnt, self.hands_card_cnt, self.won_piles_card_cnt)

    @property
    def hands_card_cnt(self) -> int:
        return sum([h.card_cnt for h in self.hands])

    @property
    def won_piles_card_cnt(self) -> int:
        return sum([p.card_cnt for p in self.won_piles])

    @property
    def played_cards_cnt(self) -> int:
        return self.middle.card_cnt + self.won_piles_card_cnt


@dataclass(frozen=True)
class SetbackScorer:
    won_piles: list[WonPile]
    bid: Bid
    trump: Card.suit

    @cached_property
    def points_adjustments(self) -> list[int]:
        """ Return a player-id-ordered list of score adjustments, positive or negative """
        bidder_points = self._points_by_player[self.bid.player_idx] if self.was_bid_made else self.bid.value * -1
        return [points if idx != self.bid.player_idx else bidder_points
                for idx, points in enumerate(self._points_by_player)]

    @cached_property
    def digest_by_point(self) -> dict:
        """ Return the high card, low card, jack card (if present), and a player-id-ordered list of game points """
        return {'High': self._high_card[0], 'Low': self._low_card[0],
                'Jack': self._jack_card[0] if self._jack_card else None,
                'Game': [p.game_points for p in self.won_piles]}

    @cached_property
    def was_bid_made(self) -> bool:
        return self._points_by_player[self.bid.player_idx] >= self.bid.value

    @cached_property
    def _points_by_player(self) -> list[int]:
        points = [0] * len(self.won_piles)
        winning_player_indexes = [self._high_card_player_idx, self._low_card_player_idx,
                                  self._jack_card_player_idx, self._game_points_player_idx]
        for winning_player_idx in winning_player_indexes:
            if winning_player_idx is not None:
                points[winning_player_idx] += 1
        return points

    @cached_property
    def _trump_cards_sorted(self) -> list[tuple[Card, int, int]]:
        """ Returns [Card, rank_int, player_idx] """
        return sorted([(c, c.rank_int, idx) for idx, p in enumerate(self.won_piles)
                       for c in p.cards if c.suit == self.trump], key=lambda x: x[1], reverse=True)

    @cached_property
    def _high_card(self) -> tuple[Card, int, int]:
        return self._trump_cards_sorted[0]

    @cached_property
    def _low_card(self) -> tuple[Card, int, int]:
        return self._trump_cards_sorted[-1]

    @cached_property
    def _jack_card(self) -> tuple[Card, int, int] | None:
        for (card, rank_int, player_idx) in self._trump_cards_sorted:
            if rank_int == 11:
                return card, rank_int, player_idx
        return None

    @cached_property
    def _high_card_player_idx(self) -> int:
        card, rank_int, player_idx = self._high_card
        return player_idx

    @cached_property
    def _low_card_player_idx(self) -> int:
        card, rank_int, player_idx = self._low_card
        return player_idx

    @cached_property
    def _jack_card_player_idx(self) -> int | None:
        if not self._jack_card:
            return None
        card, rank_int, player_idx = self._jack_card
        return player_idx

    @cached_property
    def _game_points_player_idx(self) -> int | None:
        game_points = sorted([(p.game_points, idx) for idx, p in enumerate(self.won_piles)],
                             key=lambda x: x[0], reverse=True)
        return game_points[0][1] if game_points[0][0] != game_points[0][1] else None

@dataclass(frozen=True)
class Play:
    action: Action
    player_idx: int
    before_state: GameState
    after_state: GameState

    def __post_init__(self):
        if self.action == Action.PLAY_CARD:
            ...
        elif self.action == Action.BID:
            ...

@dataclass
class GameState:
    grid: Grid

    def __post_init__(self):
        ...

    @cached_property
    def player_turn_idx(self) -> int:
        # who starts the action: - bidding: dealer + 1, first trick: highest_bidder, tricks 2-6: prior trick winner
        if self.is_bidding_phase:
            first_actor_idx = (self.grid.dealer_idx + 1) % self.grid.player_cnt
        elif not self.grid.won_piles_card_cnt:
            first_actor_idx = self.grid.bids.winning_bid.player_idx
        else:
            first_actor_idx = self.grid.prior_trick_winner_idx
        # how many people have acted this round
        already_acted_cnt = self.grid.bids.bid_cnt if self.is_bidding_phase else self.grid.middle.card_cnt
        # move in a rotation
        return (first_actor_idx + already_acted_cnt) % self.grid.player_cnt

    @cached_property
    def has_the_game_started(self) -> bool:
        """ Return True if the game is not over & if no one has any cards """
        return True if (not self.is_game_over and not self.grid.hands_card_cnt) else False

    @cached_property
    def is_bidding_phase(self) -> bool:
        return self.grid.bids.bid_cnt < self.grid.player_cnt

    @cached_property
    def is_round_over(self) -> bool:
        return False if self.grid.hands_card_cnt else True

    @cached_property
    def is_game_over(self) -> bool:
        return True if self.winner else False

    @cached_property
    def winner(self) -> int | None:
        """ If no one has reached the score, return None.
            If bidder reaches the score, return the bidder index.
            Else if two or more other players reach the score, return None.
            Else, return the highest score. """
        if not any([score for score in self.grid.scores if score >= GAME_UP_TO]):
            return None
        if self.grid.scores[self.grid.bids.winning_bid.player_idx] >= 15:
            return self.grid.bids.winning_bid.player_idx
        sorted_scores: list[tuple[int, int]] = sorted([(s, idx) for idx, s in enumerate(self.grid.scores)],
                                                      reverse=True)
        if sorted_scores[0][0] == sorted_scores[1][0]:
            return None
        return sorted_scores[0][1]

    @cached_property
    def possible_plays(self) -> list[Play]:
        return self.possible_bids if self.is_bidding_phase else self.possible_card_plays

    @cached_property
    def possible_card_plays(self) -> list[Play] | None:
        if self.is_game_over:
            return None
        hand = self.grid.hands[self.player_turn_idx]
        possible_cards = (hand.get_playable_cards(self.grid.trump, self.grid.middle.lead_card))
        return [self.play_card(self.player_turn_idx, card) for card in possible_cards]

    @cached_property
    def possible_bids(self) -> list[Play]:
        return [self.make_bid(self.player_turn_idx, bid) for bid in ALL_BIDS]

    def play_card(self, player_idx: int, card: Card) -> Play:
        try:
            # TODO: there's three versions of "copy" in here
            # can I figure out how to appropriately copy self.grid?!!!

            # if there haven't been any cards played, catalogue the first card for analytics purposes
            first_card_of_round = card if not self.grid.played_cards_cnt else self.grid.first_card_of_round

            # remove card from hand
            hands = deepcopy(self.grid.hands)
            hands[player_idx].cards.remove(card)
            # place card in middle
            middle_cards = self.grid.middle.cards.copy()
            middle_player_indexes = self.grid.middle.player_indexes.copy()
            middle_cards.append(card)
            middle_player_indexes.append(player_idx)
            middle = Middle(middle_cards, middle_player_indexes)

            # if first card of round, declare trump & catalogue first card of round (for analytics purposes)
            trump = card.suit if not self.grid.trump else self.grid.trump

            # declaring these here to make the Play object easier
            won_piles = deepcopy(self.grid.won_piles)
            trick_winner_idx = self.grid.prior_trick_winner_idx

            # if the trick is over, move cards from middle to won piles
            if middle.card_cnt == self.grid.player_cnt:
                trick_winner_idx = middle.get_trick_winner_idx(trump)
                won_piles[trick_winner_idx] = WonPile(won_piles[trick_winner_idx].cards + middle_cards)
                middle = Middle()

            scores = self.grid.scores[:]

            # if the round is over, adjust the scores & reset the first_card_of_round
            if not any([hand.cards for hand in hands]):
                score_adjustments = SetbackScorer(won_piles, self.grid.bids.winning_bid, trump).points_adjustments
                scores = [prior + adjustment for prior, adjustment in zip(self.grid.scores, score_adjustments)]

            return Play(action=Action.PLAY_CARD, player_idx=player_idx, before_state=self,
                        after_state=GameState(Grid(self.grid.player_cnt, self.grid.dealer_idx, hands, won_piles,
                                                   scores, middle, self.grid.bids, trump, trick_winner_idx,
                                                   first_card_of_round))
                        )
        except ValueError as ex:
            print(ex)

    def make_bid(self, player_idx: int, bid_value: int) -> Play:
        try:
            new_grid = deepcopy(self.grid)
            bid = Bid(bid_value, player_idx)
            new_grid.bids.bids.append(bid)
            validate_bids(new_grid.bids, self.grid.player_cnt)
            return Play(action=Action.BID, player_idx=player_idx, before_state=self, after_state=GameState(new_grid))
        except ValueError:
            ...
