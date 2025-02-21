from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
import inspect
from itertools import combinations
import random
from typing import Generator

from setnacki.game.setback_mini import SetbackMini
from setnacki.logic.models import GameState
from setnacki.logic.play_models import PlayRulesV1, PlayCardModel
from cardnacki.card import Card
from tqdm import tqdm

RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = 'hcds'
DECK = [f'{r}{s}' for r in RANKS for s in SUITS]



# TODO:
#  use case: run an pre-defined set of hands vs random hands a given number of times to see the outcomes
#  in all cases, a user can define a hand or a sequence of hands to SBM, run it X times and then receive an outcome


@dataclass
class SimResults:
    ...


def _convert_to_list_rank_suit(hand_repr: str | list[str] | list[Card]) -> list[str]:
    if isinstance(hand_repr, str):
        return [hand_repr[i:i + 2] for i in range(0, len(hand_repr), 2)]
    if isinstance(hand_repr, list):
        if isinstance(hand_repr[0], Card):
            return [c.rank_suit for c in hand_repr]
    return hand_repr


def run_hands_mid_game(gs: GameState, play_card_models: list[PlayCardModel], player_id: int,
                       card_to_lead: str | Card | None = None, simulation_cnt: int = 1):
    # TODO: what is even the use case for this?
    card_to_lead = card_to_lead.rank_suit if isinstance(card_to_lead, Card) else card_to_lead if card_to_lead else None
    for _ in tqdm(range(simulation_cnt), desc=inspect.currentframe().f_code.co_name):
        sbm = SetbackMini.create_from_game_state(gs, play_card_models, player_id, card_to_lead)
        sbm.play()


def run_known_hands(hand1: str | list[str] | list[Card], hand2: str | list[str] | list[Card],
                    play_card_models: list[PlayCardModel], simulation_cnt: int = 1):
    # accept many different types of hand representations or single card reps and convert into what SBM expects
    return_dict = defaultdict(dict)
    hand1 = _convert_to_list_rank_suit(hand1)
    hand2 = _convert_to_list_rank_suit(hand2)
    for card_to_lead in tqdm(hand1, desc=inspect.currentframe().f_code.co_name):
        total_net_points = 0
        for _ in range(simulation_cnt):
            sbm = SetbackMini([hand1.copy(), hand2.copy()], play_card_models, card_to_lead)
            sbm.play()
            total_net_points += sbm.net_points
        return_dict[''.join(hand1)][card_to_lead] = total_net_points
    return dict(return_dict)

def run_one_hand_v_random_hands(hand: str | list[str] | list[Card],
                                play_card_models: list[PlayCardModel], simulation_cnt: int = 1):
    return_dict = defaultdict(dict)
    hand = _convert_to_list_rank_suit(hand)
    for card_to_lead in tqdm(hand, desc=inspect.currentframe().f_code.co_name):
        total_net_points = 0
        for _ in range(simulation_cnt):
            sbm = SetbackMini([hand.copy(), []], play_card_models, card_to_lead)
            sbm.play()
            total_net_points += sbm.net_points
        return_dict[''.join(hand)][card_to_lead] = total_net_points
    return dict(return_dict)

def run_random_hands(play_card_models: list[PlayCardModel], random_hands_cnt: int = 1, simulation_cnt: int = 1) -> dict:
    return_dict = defaultdict(dict)
    deck = DECK.copy()
    for _ in tqdm(range(random_hands_cnt), desc=inspect.currentframe().f_code.co_name):
        hand1 = random.sample(deck, 6)
        for card_to_lead in hand1:
            total_net_points = 0
            for _ in range(simulation_cnt):
                sbm = SetbackMini([hand1.copy(), []], play_card_models, card_to_lead)
                sbm.play()
                total_net_points += sbm.net_points
            return_dict[''.join(hand1)][card_to_lead] = total_net_points
    return dict(return_dict)


def run_sum_14_or_len_3(play_card_models: list[PlayCardModel], simulation_cnt: int = 1):
    """The test hands are all single suit min_14_sum_or_3_cnt (4058 combos).
    4058 combos at 1000 iterations w each lead card is 25M sims, which ran in 100 min (~250k sims/min).
    This is the counts for min_14_sum_or_3_cnt ... most of these combos will never happen IRL ...
    suit_len_combo_counts = {0: 0, 1: 1, 2: 53, 3: 286, 4: 715, 5: 1287, 6: 1716}"""
    return_dict = defaultdict(dict)
    ranks = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K',
             14: 'A'}
    all_non_hearts = [f'{r}{s}' for r in RANKS for s in SUITS[1:]]
    sum_14_or_len_3 = (combo for length in range(1, 7) for combo in combinations(ranks.keys(), length)
                       if sum(combo) >= 14 or len(combo) >= 3)
    for hearts_rank_ints in tqdm(sum_14_or_len_3, desc=inspect.currentframe().f_code.co_name):
        hearts_cards = [f'{ranks.get(rank_int)}h' for rank_int in hearts_rank_ints]
        for rank_int in hearts_rank_ints:
            total_net_points = 0
            for _ in range(simulation_cnt):
                non_hearts_cards = random.sample(all_non_hearts, 6 - len(hearts_cards))
                hand: list[str] = hearts_cards + non_hearts_cards
                sbm = SetbackMini([hand.copy(), []], play_card_models, f'{ranks.get(rank_int)}h')
                sbm.play()
                total_net_points += sbm.net_points
            return_dict[hearts_rank_ints][rank_int] = round(total_net_points / simulation_cnt, 2)
    return dict(return_dict)


class SimRunnerStrategy(Enum):
    KNOWN_HANDS = run_known_hands
    FROM_GAME_STATE = run_hands_mid_game
    ONE_HAND = run_one_hand_v_random_hands
    RANDOM_HANDS = run_random_hands
    SUM14_OR_LEN3 = run_sum_14_or_len_3

    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)  # Call the stored function


# TODO: all of these need to return some stats about the simulations, the returned dict/dataclass should be consistent
#  should probably have a concept of a hand, a lead card, total net points, avg net points, sim cnt



# TODO: move these to the tests folder ... DO NOT ERASE!!

# run_known_hands(d.cards[46:], d.cards[:6], [PlayRulesV1(), PlayRulesV1()], simulation_cnt=2)
# run_known_hands('AhKhQhJhTh9h', '2s3s4s5s6s7s', [PlayRulesV1(), PlayRulesV1()], simulation_cnt=2)
#
# run_one_hand_v_random_hands('AhAsAdAcKhKs', [PlayRulesV1(), PlayRulesV1()], simulation_cnt=2)
#
# p0_hand = Pile.create_from_rank_suits(d, '5h 8h 2s As').cards
# p1_hand = Pile.create_from_rank_suits(d, 'Ks 2d 2h 4h 8s').cards
# middle = Pile.create_from_rank_suits(d, 'Jc').cards
# p0_won_pile = Pile.create_from_rank_suits(d, 'Ac Kc').cards
# p1_won_pile = []
# first_card_of_round = d.cards[25]  # Ac
# trump = 'clubs'
# gs = GameState(grid=Grid(player_cnt=2, dealer_idx=0, hands=[Hand(cards=p0_hand), Hand(cards=p1_hand)],
#                          won_piles=[WonPile(cards=p0_won_pile), WonPile(cards=p1_won_pile)], scores=[0, 0],
#                          middle=Middle(cards=middle, player_indexes=[]),
#                          bids=Bids(bids=[Bid(value=3, player_idx=1), Bid(value=0, player_idx=0)]),
#                          trump=trump, prior_trick_winner_idx=1, first_card_of_round=first_card_of_round))
# run_hands_mid_game(gs, [PlayRulesV1(), PlayRulesV1()], 0, simulation_cnt=2)
#
# run_random_hands([PlayRulesV1(), PlayRulesV1()], simulation_cnt=2)
#
# run_sum_14_or_len_3([PlayRulesV1(), PlayRulesV1()], simulation_cnt=1)

