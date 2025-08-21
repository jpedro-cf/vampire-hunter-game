from game.game import Game
from game.player import Player


class Level:
    def __init__(self, name: str, level: int, game: Game):
        self.name = name
        self.level = level
        self.enemies = {}

        self.game = game
        self.player = None

        self.enemies_per_time = 2 * level

    def run():
        pass
