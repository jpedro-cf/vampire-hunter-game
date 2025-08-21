from game.entity import Entity
from game.level import Level
from game.player import Player


class Enemy(Entity):
    def __init__(self, name, animations, surface, player: Player):
        super().__init__(name, animations, surface)
        self.player = player

    def move(self):
        return super().move()
