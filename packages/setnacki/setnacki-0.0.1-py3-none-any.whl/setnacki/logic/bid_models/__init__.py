import abc
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
import joblib
import json
from pathlib import Path
import random
from sklearn.ensemble import RandomForestRegressor
from typing import Any

from cardnacki.card import Card
from cardnacki.pile import Pile, PileProps, Deck
import numpy as np
from setnacki.game.setback_mini import SetbackMini
from .one_suit_min_14_2 import data as one_suit_min_14_data
from setnacki.logic.sim_runner_strategies import SimRunnerStrategy


ITERATION_CNT_DEFAULT = 1


# TODO: work with: aggressiveness & game context
#  [Ah 🂠, 7h 🂠, 2d 🂠, Jc 🂠, 5c 🂠, 3c 🂠] ... that's a good test case: what's better: A7 or J53 (A7)?

@dataclass
class BidEval:
    """suit (str), bid_amt (int), lead_card (Card | None)"""
    suit: str
    bid_amt: int
    lead_card: Card = None

@dataclass
class Comment:
    text: str
    date_: date = date.today()

@dataclass
class ModelResults:
    """A data class in the same shape as the JSON data where the model results should be stored"""
    p0_play_card_model: str
    p1_play_card_model: str
    lead_card_test_model: str
    teammate_cnt: int
    opponent_cnt: int
    iterations: int
    date_run: date
    comments: list[Comment]
    outcomes: Any

    def to_json(self) -> dict:
        if isinstance(self.comments, dict):
            outcomes = {' '.join(map(str, key)): value for key, value in self.outcomes.items()}
        else:
            outcomes = self.outcomes

        return {"p0_play_card_model": self.p0_play_card_model, "p1_play_card_model": self.p1_play_card_model,
                "lead_card_test_model": self.lead_card_test_model,
                "teammate_cnt": self.teammate_cnt, "opponent_cnt": self.opponent_cnt,
                "iterations": self.iterations, "date_run": date.today().isoformat(),
                "comments": [[c.date_.isoformat(), c.text] for c in self.comments],
                "outcomes": outcomes}

    @property
    def best_lead_card_k_v(self) -> tuple[str, float]:  # ex: ('Qh', 3.0)
        return max(self.outcomes.items(), key=lambda x: x[1])

    @property
    def best_lead_card(self) -> str:  # ex: 'Qh'
        return self.best_lead_card_k_v[0]

    @property
    def best_net_points(self) -> float:  # ex: 3.0
        return self.best_lead_card_k_v[1]


@dataclass
class BidModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_model_data(self, **kwargs) -> None:
        """Method to create data and store it in a resource; returns nothing"""
        raise NotImplementedError
        # TODO: should use SetbackMini to save its outcomes to ...

    @abc.abstractmethod
    def load_model_results(self) -> Any:
        ...

    @abc.abstractmethod
    def get_bid(self, cards: list[Card]) -> BidEval:
        ...

    @staticmethod
    def _suit_via_sum_rank_int(cards: list[Card]) -> str:
        """Used by some concrete classes to determine which suit to bid in"""
        suits = Counter()
        for c in cards:
            suits[c.suit] += c.rank_int
        return suits.most_common(1)[0][0]


@dataclass
class RulesV1(BidModel):
    def create_model_data(self) -> None:
        """Not applicable, as it creates a bid on the spot without using any other resource"""

    def load_model_results(self):
        """Not applicable, as it creates a bid on the spot without using any other resource"""

    def get_bid(self, cards: list[Card]) -> BidEval:
        # TODO: [As 🂠, Ah 🂠, 7h 🂠, Qd 🂠, Jd 🂠, Td 🂠] hearts 3 -> the A7 rule is hitting before QJT is evaluated
        #  '9c Kc 2d 7d Jd As' returns 2 because K9 is evaluated and returned before J72

        suit = self._suit_via_sum_rank_int(cards)

        ps = PileProps(cards, suit)

        # AJx, KJx: bid 4 & lead the highest card
        if ps.suit_has_any_ranks([14, 13]) and ps.suit_has_rank(11) and ps.suit_length >= 3:
            return BidEval(suit, 4, ps.suit_highest_card)
        # Axx+, Kxx+, Qxx+, len(AKQJT) >= 2 (except for JT), Ax w another A or K: bid 3 & lead the highest card
        if (ps.suit_has_any_ranks([14, 13, 12]) and ps.suit_length >= 3) or \
                (ps.suit_length_by_ranks([14, 13, 12, 11, 10]) >= 2 and ps.suit_length_by_ranks([14, 13, 12]) > 0) or \
                (ps.suit_has_rank(14) and ps.suit_length == 2 and (ps.has_a_non_suit_rank(14) or ps.has_a_non_suit_rank(13))):
            return BidEval(suit, 3, ps.suit_highest_card)
        # Jxx+, JT, J9, J8, J7: bid 3 & lead the 2nd highest card
        if ps.suit_has_rank(11) and (ps.suit_length == 3 or ps.suit_has_any_ranks([10, 9, 8, 7])):
            return BidEval(suit, 3, ps.suit_second_highest_card)
        # A, Ax (no other A or K), Kx, Qx, J, Jx, xxx+: bid 2 & lead the highest card
        if ps.suit_has_any_ranks([14, 13, 12, 11]) or ps.suit_length >= 3:
            return BidEval(suit, 2, ps.suit_highest_card)
        # T9, T8: bid 2 & lead the 2nd highest card
        if ps.suit_length_by_ranks([10, 9, 8]) >= 2:
            return BidEval(suit, 2, ps.suit_second_highest_card)
        # no matches: suggest a pass
        return BidEval(suit, 0, ps.suit_highest_card)


@dataclass
class SingleSuitLookUp(BidModel):
    """Model keys are rank ints for a single suit where the sum >= 14 or the length >= 3 (4508 combos, 25k rank ints).
    get_bid() uses an external best suit finder & looks up the best suit's rank ints in the model dict.
    If no match, it's assumed to be a pass and returns BidEval(suit, 0, highest_suit_card).
    If the suit's rank_int combo is found, returns BidEval(suit, a bid amount, best_lead_card)"""
    _model_results: dict = field(init=False)
    _resource_name: str = 'one_suit_min_14.py'

    # TODO: _resource_name is used to create the model, but pulling in the model results just imports from a python file
    #  not sure this is a problem, as it might be different for an ML model

    def __post_init__(self):
        self._model_results = self.load_model_results()

    def create_model_data(self, p0_pcm, p1_pcm, sim_cnt: int = 1) -> dict:
        """Uses SimRummerStrategy.Sum14_or_Len_3 and returns a dictionary ex:
        {(14,): {14: 1}, (2, 12): {2: 1, 12: 3}, (2, 13): {2: -1, 13: 1}}"""
        hand_lead_card_dict: dict = SimRunnerStrategy.SUM14_OR_LEN3([p0_pcm, p1_pcm], sim_cnt)
        d = {}
        # TODO: this was previously expecting the key like 'AhKh...' but it's now a sorted tuple of hearts rank ints
        #  modify the below code to accommodate
        for hand, lead_card_stats in hand_lead_card_dict.items():
            heart_rank_strs = [rs[0] for rs in [hand[i:i + 2] for i in range(0, len(hand), 2)] if rs[-1] == 'h']
            ranks = (None, None, '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
            rank_ints = tuple(sorted(ranks.index(rank_str) for rank_str in heart_rank_strs))
            stats = {ranks.index(rank_str[0]): net_points for rank_str, net_points in lead_card_stats.items()}
            d[rank_ints] = stats
        return d

    def write_data_to_py_file(self, data: dict, file_name: str = None) -> None:
        """Loading from .py is faster and smaller on disk than .json"""
        file_name = file_name or self._resource_name
        if file_name == self._resource_name:
            if input(f'Warning: {file_name} already exists. Definitely overwrite its contents? (Y/n) ') != 'Y':
                return
        with open(file_name, 'w') as f:
            f.write('data = {\n')
            for k, v in data.items():
                f.write(f'{k}: {v},\n')
            f.write('}\n')

    @staticmethod
    def load_model_results() -> dict:
        return one_suit_min_14_data

    def get_bid(self, cards: list[Card]) -> BidEval:
        suit = self._suit_via_sum_rank_int(cards)
        ps = PileProps(cards, suit)
        rank_int_lookup_key = tuple(sorted(ps.suit_rank_ints))
        lead_card_dict: dict[int: float] = self._model_results.get(rank_int_lookup_key)

        if not lead_card_dict:
            return BidEval(suit, 0, ps.suit_highest_card)

        best_lead_card_str, net_points = max(lead_card_dict.items(), key=lambda x: (x[1], x[0]))

        # TODO: rework this dictionary into aggressiveness
        net_points_bid_amt = {3.5: 4, 2.1: 3, 1.0: 2}
        bid_amt = next((v for k, v in net_points_bid_amt.items() if net_points >= k), 0)

        return BidEval(suit, bid_amt, next(c for c in ps.suit_cards if c.rank_int == int(best_lead_card_str)))


@dataclass
class RandForestRegressor(BidModel):
    model_results: ModelResults = field(init=False)

    def __post_init__(self):
        self.model_results = self.load_model_results()

    def create_model_data(self, p0_pcm, p1_pcm, lead_card_test_model, file_name: str,
                          teammate_cnt: int = 0, opponent_cnt: int = 1,
                          iterations_per_hand: int = 1, iterations_per_lead_card: int = 1000,
                          comments: list[Comment] = None) -> None:

        if not comments:
            comments = [Comment('Initial Run')]

        outcomes = []
        d = Deck()
        for _ in range(iterations_per_hand):
            random_hand: list[Card] = random.sample(d.cards, 6)

            for lead_card in random_hand:
                hand_list_str: list[str] = Pile(random_hand).to_rank_suits().split()
                total_net_points = 0
                for _ in range(iterations_per_lead_card):
                    sbm = SetbackMini([hand_list_str.copy(), []], [p0_pcm, p1_pcm], lead_card.rank_suit)
                    sbm.play()
                    total_net_points += sbm.net_points
                feature_matrix = self._create_feature_matrix(random_hand, lead_card)
                net_points = round(total_net_points / iterations_per_lead_card, 1)
                outcomes.append([feature_matrix, net_points])

        model_results_json = ModelResults(p0_pcm.__class__.__name__, p1_pcm.__class__.__name__,
                                          lead_card_test_model.__class__.__name__,
                                          teammate_cnt, opponent_cnt,
                                          iterations_per_hand, date.today(), comments, outcomes).to_json()

        print(model_results_json)
        if input(f'Are you sure you want to write fresh to file: {file_name}? (Y/n) ') == 'Y':
            with open(file_name, 'w') as f:
                json.dump(model_results_json, f, indent=4, separators=(", ", ": "))

        if input(f'Do you want to write the model to a pickle file?  (Y/n) ') == 'Y':
            self.write_pickled_model()

    def write_pickled_model(self, file_name: str = 'rand_forest_model.pkl'):
        X = np.array([res[0] for res in self.model_results.outcomes])  # Feature matrix
        y = np.array([res[1] for res in self.model_results.outcomes])  # Target vector
        model = RandomForestRegressor()
        model.fit(X, y)

        current_dir = Path(__file__).parent.resolve()
        file_path = current_dir / file_name
        joblib.dump(model, file_path)

    @staticmethod
    def _create_feature_matrix(cards: list[Card], lead_card: Card) -> list[int]:
        """Lead card goes first, all other cards of lead suit are placed next (rank_int asc), all others are placed last.
        lead suit cards are converted to 1, non-lead suit cards are converted to 0.
        Example input & return: ['7h', 'Tc', '9s', 'As', '7s', '3c'] -> [7, 1, 14, 1, 9, 1, 10, 0, 7, 0, 3, 0]."""
        ordered = sorted(cards,
                         key=lambda card: (card == lead_card, card.suit == lead_card.suit, card.rank_int),
                         reverse=True)
        encoded = []
        for c in ordered:
            encoded.append(c.rank_int)
            encoded.append(1) if c.suit == lead_card.suit else encoded.append(0)
        return encoded

    def load_model_results(self, file_name: str = 'rand_forest_regressor.json') -> ModelResults:
        current_dir = Path(__file__).parent.resolve()
        file_path = current_dir / file_name
        with open(file_path, 'r') as f:
            data = json.load(f)
            return ModelResults(**data)

    @staticmethod
    def get_pickled_model(file_name: str = 'rand_forest_model.pkl') -> RandomForestRegressor:
        current_dir = Path(__file__).parent.resolve()
        file_path = current_dir / file_name
        return joblib.load(file_path)

    def get_bid(self, cards: list[Card]) -> BidEval:
        """Load model, make a prediction for leading each card, return BidEval(suit, bid_amt, best_lead_card)"""
        model = self.get_pickled_model()

        # 2c: for all cards, get the model's predicted net points ... run the model
        lead_card_net_points = []
        for c in cards:
            feature_matrix = self._create_feature_matrix(cards, c)

            # Ensure the input is a 2D array
            feature_matrix = np.array(feature_matrix).reshape(1, -1)  # Reshape to (1, n_features)

            # Predict the float value
            net_points = model.predict(feature_matrix)
            lead_card_net_points.append((c, net_points))

        best_lead_card, net_points = max(lead_card_net_points, key=lambda x: x[1])

        net_points_to_bid_amt = {(-float('inf'), 0.9): 0, (1.0, 2.0): 2, (2.1, 3.4): 3, (3.5, 4.0): 4}
        bid_amt = next(v for ((min_, max_), v) in net_points_to_bid_amt.items() if min_ <= net_points <= max_)

        return BidEval(best_lead_card.suit, bid_amt, best_lead_card)


if __name__ == "__main__":
    ...
