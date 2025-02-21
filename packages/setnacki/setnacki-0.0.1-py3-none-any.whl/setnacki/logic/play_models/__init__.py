import abc
from dataclasses import dataclass, field

from cardnacki.card import Card
from setnacki.logic.models import WonPile

@dataclass
class CardSelectionProps:
    playable_cards: list[Card]
    lead_card: Card | None
    trump: str
    won_piles: list[WonPile]  # currently only using own won pile but could expand to gain knowledge of low, for ex.
    id_: int  # to know which thrown cards were thrown by whom
    
    @property
    def is_leader(self) -> bool:
        return self.lead_card is None

    @property
    def has_trump(self) -> bool:
        return self.trump in [c.suit for c in self.playable_cards]

    @property
    def trump_cards(self) -> list[Card]:
        return [c for c in self.playable_cards if c.suit == self.trump]

    @property
    def trump_rank_ints(self) -> list[int]:
        return [c.rank_int for c in self.playable_cards if c.suit == self.trump]

    @property
    def higher_ranks_in_suit(self) -> list[Card]:
        return sorted([c for c in self.playable_cards if c.suit == self.lead_card.suit
                       and c.rank_int > self.lead_card.rank_int], key=lambda x: x.rank_int)

    @property
    def suits_opponent_does_not_have(self) -> list[str]:
        """Comb your own won pile, two cards at a time, check for tricks where the opponent didn't follow.
        If you threw non-trump & they trumped, that trick wouldn't be in your pile"""
        if not self.won_piles[self.id_]:
            return []
        suits_they_dont_have = set()
        for lead, follow in zip(self.won_piles[self.id_], self.won_piles[self.id_].cards[1:]):
            if lead.suit != follow.suit and follow.suit != self.trump:
                suits_they_dont_have.add(lead.suit)
        return list(suits_they_dont_have)

    @property
    def is_opponent_trumped(self) -> bool:
        if not self.suits_opponent_does_not_have:
            return False
        return True if self.trump in self.suits_opponent_does_not_have else False

    @property
    def highest_non_ten_else_ten(self) -> Card | None:
        if hntet := sorted([c for c in self.playable_cards if c.suit != self.trump],
                           key=lambda x: (x.rank_int == 10, -x.rank_int)):
            return hntet[0]
        return None

    @property
    def lowest_non_ten_else_ten(self) -> Card | None:
        """Worst non-trump card"""
        if lntet := sorted([c for c in self.playable_cards if c.suit != self.trump],
                           key=lambda x: (x.rank_int == 10, x.rank_int)):
            return lntet[0]
        return None

    @property
    def highest_trump(self) -> Card:
        if not self.has_trump:
            raise ValueError("You are trying to play the lowest card but don't have any")
        return sorted(self.trump_cards, key=lambda x: x.rank_int, reverse=True)[0]

    @property
    def lowest_trump(self) -> Card:
        if not self.has_trump:
            raise ValueError("You are trying to play the lowest card but don't have any")
        return sorted(self.trump_cards, key=lambda x: x.rank_int)[0]

    @property
    def non_trump_card_where_opponent_doesnt_have_that_suit(self) -> Card | None:
        """If opponent is known to be out of a certain non-trump suit & we have such a card, return any such card,
        else None"""
        if not self.suits_opponent_does_not_have:
            return None
        for suit in self.suits_opponent_does_not_have:
            if suit != self.trump and suit in [c.suit for c in self.playable_cards]:
                return next(c for c in self.playable_cards if c.suit == suit)
        return None

    @property
    def can_win_trick(self) -> bool:
        if not self.lead_card:
            return True
        if self.higher_ranks_in_suit or (self.lead_card.suit != self.trump and self.has_trump):
            return True
        return False
    

@dataclass
class PlayCardModel(metaclass=abc.ABCMeta):
    """Note: this relies on there being trump already established;
    didn't factor in that this could be the first card, since I'm expecting that from the bid model."""

    @abc.abstractmethod
    def select_card(self, *args) -> Card:
        """Concrete class must implement this method. It may have different arguments but must return a Card"""


class PlayRulesV1(PlayCardModel):
    @staticmethod
    def select_card(playable_cards: list[Card], lead_card: Card | None,
                    trump: str, won_piles: list[WonPile], id_: int) -> Card:
        csp = CardSelectionProps(playable_cards, lead_card, trump, won_piles, id_)
        # Leader Logic
        if csp.is_leader:
            # L has AKQ98765TJ of Trump, F may have trump, throw trump card in that order.
            if csp.has_trump and csp.trump_rank_ints not in ([2], [3], [4]) and not csp.is_opponent_trumped:
                return sorted(csp.trump_cards, key=lambda x: (x.rank_int == 11, x.rank_int == 10, -x.rank_int))[0]
            # F is out of a non-trump suit & L has that suit, throw it
            if such_a_card := csp.non_trump_card_where_opponent_doesnt_have_that_suit:
                return such_a_card
            # Play highest non-trump, non-ten, else ten, else highest trump
            return csp.highest_non_ten_else_ten or csp.highest_trump

        # Follower Logic
        else:
            # L is not trump
            if csp.lead_card.suit != csp.trump:
                if not csp.can_win_trick:
                    # F cannot win trick.  Throw lowest non-ten rank.
                    return csp.lowest_non_ten_else_ten
                # if you can win the trick w a T of the lead suit, do so
                if 10 in [c.rank_int for c in csp.higher_ranks_in_suit]:
                    return next(c for c in csp.higher_ranks_in_suit if c.rank_int == 10)
                # L throws T, take it with the next best card in that suit or lowest trump
                if csp.lead_card.rank_int == 10:
                    return csp.higher_ranks_in_suit[0] if csp.higher_ranks_in_suit else csp.lowest_trump
                # L throws J or Q, play Q/K/A else worst card else lowest trump
                if csp.lead_card.rank_int in (11, 12):
                    return csp.higher_ranks_in_suit[0] if csp.higher_ranks_in_suit else csp.lowest_non_ten_else_ten or csp.lowest_trump
                # L throws K or A, win w A else throw the lowest trump
                if csp.lead_card.rank_int in (13, 14) and csp.has_trump:
                    return csp.higher_ranks_in_suit[0] if csp.higher_ranks_in_suit else csp.lowest_trump
                # L throws 2-9, try to lose trick
                return csp.lowest_non_ten_else_ten or csp.lowest_trump

            # L is trump
            else:
                # if no trump, throw worst card
                if not csp.has_trump:
                    return csp.lowest_non_ten_else_ten
                # L throws K, J, T, 3, 2, take trick
                least_valuable_trump = sorted([c for c in csp.playable_cards],
                                              key=lambda x: (x.rank_int == 11, x.rank_int == 2, x.rank_int == 10, x.rank_int == 3,
                                              x.rank_int == 14, x.rank_int == 13, x.rank_int == 12, -x.rank_int))[0]
                if csp.lead_card.rank_int in (13, 11, 10, 3, 2):
                    return csp.higher_ranks_in_suit[0] if csp.higher_ranks_in_suit else least_valuable_trump
                # L throws A, Q, 9-4, play your trump cards in this order 987654QKA3T2J
                return least_valuable_trump

            # TODO: AJ2, the J is consistently showing as the best card to lead ...
            #  ex: {'AhJh2h8c8d8s': {'Ah': 62728, 'Jh': 66998, '2h': 44415, '8c': -18610, '8d': -18474, '8s': -18525}}

class MonteCarlo(PlayCardModel):
    def select_card(self, playable_cards: list[Card], lead_card: Card | None,
                    trump: str, won_piles: list[WonPile], id_: int) -> Card:
        raise NotImplementedError

        csp = CardSelectionProps(playable_cards, lead_card, trump, won_piles, id_)

        # TODO:
        #  card selection props seems to have a way to reconstruct context (like is_opp_trumped) on the spot ...
        #  does it require SetbackMini to know that or can it use how the main game assigns cards to the won piles?
