import random
import uuid

from pygame import Surface
from game.character_spritesheet import Animations
from game.const import SCREEN_HEIGHT, SCREEN_WIDTH
from game.enemy import Enemy
from game.loots import DamageLoot, HealthLoot, SpeedLoot
from game.player import Player


class CharacterFactory:
    @staticmethod
    def get_entity(type: str, level: int, surface: Surface):
        match type:
            case "enemy":
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)

                name = "enemy" + str(uuid.uuid4())
                enemy = Enemy(name, Animations().enemy_animations, surface)

                enemy.x, enemy.y = x, y

                base_speed = 1
                base_damage = 25

                enemy.damage = base_damage + 10 * (level - 1)  # 10 por nivel
                enemy.speed = base_speed + 0.25 * (level - 1)  # 0.25 por nivel

                return enemy

            case "player":
                player = Player(
                    "player", Animations().player_animations, surface, 150, 150
                )
                return player

            case "loot":
                name = str(uuid.uuid4())
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)

                objects = {
                    1: SpeedLoot(name, "speed", surface, x, y),
                    2: HealthLoot(name, "health", surface, x, y),
                    3: DamageLoot(name, "damage", surface, x, y),
                }

                index = random.randint(1, 3)

                return objects[index]
