import math
from game.character import Character


class CharacterMediator:

    @staticmethod
    def verify_attack(character: Character, target: Character):
        if character.state != "attack":
            return

        if character.animation.i < len(character.animation.images):
            return

        dx = target.x - character.x
        dy = target.y - character.y
        distance = math.hypot(dx, dy)

        attack_range = 40

        if distance <= attack_range:
            target.hurt()
            target.health -= character.damage

        if target.health <= 0:
            target.die()
