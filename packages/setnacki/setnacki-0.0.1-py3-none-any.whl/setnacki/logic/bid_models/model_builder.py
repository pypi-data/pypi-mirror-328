from copy import deepcopy

from cardnacki.card import Card
from cardnacki.pile import Deck
from setback_mini_old import SetbackMini


# TODO: everything.  this isn't being used. is it a model factory?  should it return a model?


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

def _test_hand(cards: list[Card], iteration_cnt: int, best_suit: str) -> dict:
    the_hands = [cards, []]
    trump_cards = [c for c in the_hands[0] if c.suit == best_suit]
    hand = tuple([c.rank_suit for c in the_hands[0]])
    results = {hand: {}}

    for lead_card in trump_cards:
        my_points = their_points = net_points = made_2 = made_3 = made_4 = 0

        for _ in range(iteration_cnt):
            game = SetbackMini(deepcopy(the_hands), lead_card)
            game.play()
            my_points += game.points[0]
            their_points += game.points[1]
            net_points += game.points[0] - game.points[1]
            made_2 += game.points[0] >= 2
            made_3 += game.points[0] >= 3
            made_4 += game.points[0] >= 4

        lead_card = lead_card.rank_suit
        results[hand][lead_card] = {'iterations': iteration_cnt, 'my_points': my_points, 'their_points': their_points,
                                    'net_points': net_points, 'made_2': made_2, 'made_3': made_3, 'made_4': made_4}

    return results


def _get_net_points_and_best_lead_card(sim_results: dict) -> tuple[float, Card]:
    deck = Deck()
    max_net_points = -float('inf')
    best_lead_card_rank_str = ''
    for lead_card, sim_data in sim_results.values():
        if net_points := sim_data['net_points'] / sim_data['iterations'] > max_net_points:
            max_net_points = net_points
            best_lead_card_rank_str = lead_card
    best_lead_card = next(c for c in deck.cards if c.rank_str == best_lead_card_rank_str)
    return max_net_points, best_lead_card


def _run_hand_sim(hand: list[Card], iteration_cnt: int, best_suit: str) -> list[tuple[list[int], float]]:
    hands_and_points = []
    # while True:
    #     hand = random.sample(card_ints, 6)  # Randomly select 6 unique numbers
    #     if any(n >= 40 for n in hand):  # Check if at least one number is 40 or higher
    #         break  # Exit the loop if the condition is satisfied

    results = test_hand(hand, iteration_cnt=1000, best_suit=best_suit)
    for hand, values in results.items():
        print(i, hand, time.time())
        for lead_card, data in values.items():
            hands_and_points.append((encode_cards_w_order(hand, lead_card), data['net_points'] / data['iterations']))
    return hands_and_points
