# this is where the main loop goes
# and establish the abstract game engine leveraged by the front end

# requirements:
# - x players
# - play area
# - rules

from dataclasses import dataclass
import random
from typing import Callable, TypeAlias

from setnacki.game.players import Player
from setnacki.game.renderers import Renderer
from setnacki.logic.models import Bid, Bids, GameState, Grid, Hand, Middle, SetbackScorer, SetbackDeck, WonPile
from setnacki.logic.validators import validate_player_cnt

ErrorHandler: TypeAlias = Callable[[Exception], None]

@dataclass(frozen=True)
class Setback:
    players: list[Player]
    renderer: Renderer
    play_up_to: int = 0
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_player_cnt(self.player_cnt)

    @property
    def player_cnt(self) -> int:
        return len(self.players)

    @property
    def initial_dealer_idx(self) -> int:
        return random.choice([i for i in range(self.player_cnt)])

    def deal(self) -> list[Hand]:
        deck = SetbackDeck()
        deck.shuffle()
        hands = [Hand() for _ in range(self.player_cnt)]
        for hand in hands:
            for _ in range(6):
                hand.cards.append(deck.cards.pop())
        return hands

    def deal_w_test_hand(self, test_hand: Hand) -> list[Hand]:
        deck = SetbackDeck()
        [deck.cards.remove(c) for c in test_hand.cards]
        deck.shuffle()
        hands = [test_hand if i == 0 else Hand() for i in range(self.player_cnt)]
        for hand in hands[1:]:
            for i in range(6):
                hand.cards.append(deck.cards.pop())
        return hands

    def play(self) -> None:
        game_state = self.create_new_game()

        while True:
            while True:
                self.renderer.render(game_state, self.players)
                if game_state.is_round_over:
                    break
                player = self.get_current_player(game_state)
                try:
                    game_state = player.make_move(game_state)
                except ValueError as ex:
                    if self.error_handler:
                        self.error_handler(ex)

            if game_state.is_game_over:
                break

            game_state = self.create_new_round(game_state)

    def play_test_hand(self, test_hand: Hand) -> tuple[GameState, SetbackScorer]:
        game_state = self.create_test_game(test_hand)
        while True:
            if game_state.is_round_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except ValueError as ex:
                if self.error_handler:
                    self.error_handler(ex)
        scorer = SetbackScorer(game_state.grid.won_piles, game_state.grid.bids.winning_bid, game_state.grid.trump)
        return game_state, scorer

    def create_test_game(self, test_hand: Hand) -> GameState:
        initial_dealer_idx = 1
        hands = self.deal_w_test_hand(test_hand)
        won_piles = [WonPile() for _ in range(self.player_cnt)]
        scores = [0 for _ in range(self.player_cnt)]
        bids = Bids([Bid(2, 0), Bid(0, 1)])
        return GameState(Grid(self.player_cnt, initial_dealer_idx, hands, won_piles, scores, Middle(), bids))

    def get_current_player(self, game_state: GameState) -> Player:
        return self.players[game_state.player_turn_idx]

    def create_new_game(self) -> GameState:
        hands = self.deal()
        won_piles = [WonPile() for _ in range(self.player_cnt)]
        scores = [0 for _ in range(self.player_cnt)]
        return GameState(Grid(self.player_cnt, self.initial_dealer_idx, hands, won_piles, scores))

    def create_new_round(self, game_state: GameState) -> GameState:
        dealer_idx = (game_state.grid.dealer_idx + 1) % self.player_cnt
        hands = self.deal()
        won_piles = [WonPile() for _ in range(self.player_cnt)]
        return GameState(Grid(self.player_cnt, dealer_idx, hands, won_piles, game_state.grid.scores))

# SHOULD I CREATE A GAME LOG / GAME STATE STACK??
