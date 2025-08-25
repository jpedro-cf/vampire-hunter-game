from game.object import Object
from game.player import Player


class SpeedLoot(Object):
    def __init__(self, name, type, surface, x, y):
        image = "./assets/loots/speed.png"

        super().__init__(name, type, surface, image, x, y)

    def apply_effect(self, target):
        if not isinstance(target, Player) or self.target is not None:
            return

        self.target = target

        self.target.speed *= 1.5

        super().apply_effect(target)

    def remove_effect(self):
        self.target.speed /= 1.5


class DamageLoot(Object):
    def __init__(self, name, type, surface, x, y):
        image = "./assets/loots/damage.png"
        super().__init__(name, type, surface, image, x, y)

    def apply_effect(self, target):
        if not isinstance(target, Player) or self.target is not None:
            return

        self.target = target

        self.target.damage *= 1.5

        super().apply_effect(target)

    def remove_effect(self):
        self.target.damage /= 1.5


class HealthLoot(Object):
    def __init__(self, name, type, surface, x, y):
        image = "./assets/loots/health_potion.png"
        super().__init__(name, type, surface, image, x, y)

    def apply_effect(self, target):
        if not isinstance(target, Player) or self.target is not None:
            return

        self.target = target

        self.target.health *= 1.5

        super().apply_effect(target)

    def remove_effect(self):
        return
