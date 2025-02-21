import abc
from setnacki.game.players import Player
from setnacki.logic.models import GameState


class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, game_state: GameState, players: list[Player]) -> None:
        """Render the current game state & player information"""
