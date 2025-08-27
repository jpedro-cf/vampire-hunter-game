import random
import uuid

from pygame import Rect, Surface
from game.character_spritesheet import Animations
from game.const import SCREEN_HEIGHT, SCREEN_WIDTH
from game.enemy import Enemy
from game.loots import DamageLoot, HealthLoot, SpeedLoot
from game.player import Player


class CharacterFactory:
    @staticmethod
    def get_entity(type: str, level: int, surface: Surface, play_area: Rect):
        match type:
            case "enemy":
                x = random.randint(play_area.left, play_area.right)
                y = random.randint(play_area.top, play_area.bottom)

                name = "enemy" + str(uuid.uuid4())
                enemy = Enemy(name, Animations().enemy_animations, surface, play_area)

                enemy.x, enemy.y = x, y

                base_speed = 1
                base_damage = 25

                enemy.damage = base_damage + 10 * (level - 1)  # 10 por nivel
                enemy.speed = base_speed + 0.25 * (level - 1)  # 0.25 por nivel

                return enemy

            case "player":
                player = Player(
                    "player",
                    Animations().player_animations,
                    surface,
                    play_area.centerx,
                    play_area.centery,
                    play_area,
                )
                return player

            case "loot":
                name = str(uuid.uuid4())
                x = random.randint(play_area.left + 64, play_area.right - 64)
                y = random.randint(play_area.top + 64, play_area.bottom - 64)

                objects = {
                    1: SpeedLoot(name, "speed", surface, x, y),
                    2: HealthLoot(name, "health", surface, x, y),
                    3: DamageLoot(name, "damage", surface, x, y),
                }

                index = random.randint(1, 3)

                return objects[index]
