import math
from game.character import Character
from game.object import Object


class CharacterMediator:

    @staticmethod
    def verify_attack(character: Character, target: Character):
        if not character:
            return

        if character.state != "attack" or target.state == "death":
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

    @staticmethod
    def verify_collision(character: Character, obj: Object):
        dx = obj.x - character.x
        dy = obj.y - character.y
        distance = math.hypot(dx, dy)

        collision_radius = 30

        if distance > collision_radius:
            return False

        obj.apply_effect(character)
        return True
