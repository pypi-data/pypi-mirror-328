from __future__ import annotations

from typing import TYPE_CHECKING

# the TYPE_CHECKING constant is False at run-time but 3rd party tools like MyPy
# will pretend it's true when performing static type checking to allow the import statement to run
# however because you no longer import the required type at run-time, you must
# now use forward declarations or take advantage of from __future__ import annotations
# which will turn annotations into string literals

if TYPE_CHECKING:
    from setnacki.game.engine import Setback
    from setnacki.logic.models import Action, Bid, Bids, Grid, Hand, Middle, Play, SetbackDeck, WonPile

ALL_BIDS = [0, 2, 3, 4]

def validate_bid(bid: Bid):
    if bid.value not in ALL_BIDS:
        raise ValueError("Your bid is invalid")

def validate_bids(bids: Bids, player_cnt: int):
    """ If all players have bid, all bids cannot be zero.
        Each non-zero bid must be higher than the last. """
    if not bids.bid_cnt:
        return

    non_zero_bid_values = [v.value for v in bids.bids if v.value > 0]

    if bids.bid_cnt == player_cnt:
        if not non_zero_bid_values:
            raise ValueError("The dealer is forced to bid")

    if len(non_zero_bid_values) != len(set(non_zero_bid_values)):
        raise ValueError("You cannot bid the same as an existing bid")

    if non_zero_bid_values != sorted(non_zero_bid_values):
        raise ValueError("You cannot bid less than the current highest bid")

def validate_card_cnt(grid: Grid):
    if not (grid.hands_card_cnt + grid.won_piles_card_cnt + grid.middle.card_cnt) == 6 * grid.player_cnt:
        raise ValueError(f"The cards in hands, the middle, and the won pile don't add up")

def validate_hand(hand: Hand):
    if not 0 <= hand.card_cnt <= 6:
        raise ValueError("The hand doesn't have between 0 and 6 cards")

def validate_hands(hands: list[Hand]):
    smallest, *middle, largest = sorted([h.card_cnt for h in hands])
    if smallest < largest - 1:
        raise ValueError("There is a hand with two fewer cards than another")
    # should probably also validate the same card isn't in two different hands

def validate_middle(middle: Middle):
    if middle.card_cnt not in (0, 1, 2):
        raise ValueError("The Middle must have 0, 1, or 2 cards")

def validate_play(play: Play):
    ...

def validate_player_cnt(player_cnt: int):
    if not 2 <= player_cnt <= 4:
        raise ValueError("A game must be 2, 3, or 4 players")

def validate_setback_deck(d: SetbackDeck):
    if not sum(c.attributes['game_points'] for c in d['Ah Th 2s']) == 14:
        raise ValueError("Setback Deck did not correctly set game points")

def validate_won_pile(won_pile: WonPile):
    if not 0 <= won_pile.card_cnt <= 12:
        raise ValueError("Won Pile must have between 0 and 12 cards")

def validate_won_piles(player_cnt: int, hand_card_cnt: int, won_pile_card_cnt: int):
    ...
