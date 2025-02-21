import abc
import time

from setnacki.logic.models import Card, Bid, Bids, GameState, Play
from setnacki.logic.bid_models import BidEval, BidModel, RulesV1, RandForestRegressor
from setnacki.logic.play_models import PlayCardModel, PlayRulesV1


class Player(metaclass=abc.ABCMeta):
    def __init__(self, id_: int, name: str) -> None:
        self.id_ = id_
        self.name = name

    def make_move(self, game_state: GameState) -> GameState:
        # if the game state is somthing like "evaluating", then no input should be accepted ...

        if game_state.is_bidding_phase:
            if self.id_ == game_state.player_turn_idx:
                if bid := self.get_bid(game_state):
                    return bid.after_state
            raise ValueError("It's not your turn")
        else:
            if self.id_ == game_state.player_turn_idx:
                if move := self.get_play(game_state):
                    return move.after_state
            else:
                raise ValueError("It's not your turn")

    @abc.abstractmethod
    def get_bid(self, game_state: GameState) -> Bid | None:
        """Return the current player's bid in the given game state"""

    @abc.abstractmethod
    def get_play(self, game_state: GameState) -> Play | None:
        """Return the current player's play in the given game state"""

class HumanPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, id_: int, name: str):
        super().__init__(id_, name)

    @abc.abstractmethod
    def get_bid(self, game_state: GameState) -> Play | None:
        """Return the human's bid in the given game state"""

    @abc.abstractmethod
    def get_play(self, game_state: GameState) -> Play | None:
        """Return the human's play in the given game state"""


class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, id_: int, name: str, bid_model: BidModel, play_card_model: PlayCardModel,
                 delay_seconds: float = 0.25) -> None:
        super().__init__(id_, name)
        self.delay_seconds = delay_seconds
        self.bid_model: BidModel = bid_model
        self.bid_eval: BidEval | None = None
        self.play_card_model: PlayCardModel = play_card_model
        self.attributes = {}

    def get_bid(self, game_state: GameState) -> Play | None:
        """Bids 2 on a forced bid and passes on a forced pass.
        If the desired bid does not exceed the existing bid, pass. Note: this should be deferred to each Bot!!!"""
        try:
            time.sleep(self.delay_seconds)
            existing_bids: Bids = game_state.grid.bids
            if existing_bids.winning_bid_int == 0 and existing_bids.bid_cnt == game_state.grid.player_cnt - 1:
                self.bid_eval = self.bid_model.get_bid(game_state.grid.hands[self.id_].cards)
                return game_state.make_bid(self.id_, 2)
            if len(game_state.possible_bids) == 1:
                # self.bid_eval = self.bid_model.get_bid(game_state.grid.hands[self.id_].cards)
                return game_state.make_bid(self.id_, game_state.possible_bids[0].after_state.grid.bids.bids[-1].value)

            self.bid_eval = self.bid_model.get_bid(game_state.grid.hands[self.id_].cards)
            desired_bid_amt = self.bid_eval.bid_amt
            bid_amt = desired_bid_amt if desired_bid_amt > game_state.grid.bids.winning_bid_int else 0
            return game_state.make_bid(self.id_, bid_amt)
        except:
            raise ValueError("Something has gone wrong with bidding")

    def get_play(self, game_state: GameState) -> Play | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_play(game_state)

    def get_computer_play(self, game_state: GameState) -> Play | None:
        """Return the computer's play in the given game state.
        If only one legal move, play that card.
        Else, send the play_card_model func: playable cards, lead card, trump & won piles & id_.
        Model returns a Card and function returns a Play."""
        try:
            playable_cards = game_state.grid.hands[self.id_].get_playable_cards(game_state.grid.trump,
                                                                                game_state.grid.middle.lead_card)
            if len(playable_cards) == 1:
                return game_state.play_card(self.id_, playable_cards[0])

            card_to_play = self.get_computer_play_card(game_state, playable_cards)
            return game_state.play_card(self.id_, card_to_play)
        except:
            raise ValueError("Something has gone wrong with playing a card")

    @abc.abstractmethod
    def get_computer_play_card(self, *args):
        """Concrete implementer determines what args it must send to its play_card_model.select_card()"""


class Alphonso(ComputerPlayer):
    """Bid model is rules_v1. If bidder & throwing first card, plays suggested lead card, else random."""
    def __init__(self, id_: int):
        super().__init__(id_, name=self.__class__.__name__, bid_model=RulesV1(), play_card_model=PlayRulesV1())

    def get_computer_play_card(self, game_state: GameState, playable_cards) -> Card:
        """If bid won and trick #1 and there is a suggested lead card, lead that.
        Else, use game state & playable cards to select a card from PlayRulesV1"""
        try:
            if not game_state.is_bidding_phase and not game_state.grid.played_cards_cnt and self.bid_eval.lead_card:
                return self.bid_eval.lead_card

            return self.play_card_model.select_card(playable_cards, game_state.grid.middle.lead_card,
                                                    game_state.grid.trump, game_state.grid.won_piles, self.id_)
        except IndexError:
            return None


class Berto(ComputerPlayer):
    """Bid model is random_forest_regressor.
    If bidder & throwing first card, plays suggested lead card, else uses play rules v1."""
    def __init__(self, id_: int):
        super().__init__(id_, name=self.__class__.__name__, bid_model=RandForestRegressor(), play_card_model=PlayRulesV1())

    def get_computer_play_card(self, game_state: GameState, playable_cards) -> Card:
        """If bid won and trick #1 and there is a suggested lead card, lead that.
        Else, use game state & playable cards to select a card from PlayRulesV1"""
        try:
            if not game_state.is_bidding_phase and not game_state.grid.played_cards_cnt and self.bid_eval.lead_card:
                return self.bid_eval.lead_card

            return self.play_card_model.select_card(playable_cards, game_state.grid.middle.lead_card,
                                                    game_state.grid.trump, game_state.grid.won_piles, self.id_)
        except IndexError:
            return None
