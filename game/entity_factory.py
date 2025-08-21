import random
from game.character_spritesheet import Animations
from game.const import SCREEN_HEIGHT, SCREEN_WIDTH
from game.enemy import Enemy
from game.level import Level
from game.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(type: str, level: Level):
        match type:
            case "enemy":
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)

                name = "enemy" + len(level.enemies) + 1
                enemy = Enemy(
                    name, Animations().enemy_animations, level.game.window, level.player
                )

                enemy.x, enemy.y = x, y

                base_speed = 1
                base_damage = 10

                enemy.damage = base_damage + 5 * (level.level - 1)  # 5 por nivel
                enemy.speed = base_speed + 0.2 * (level.level - 1)  # 0.2 por nivel

            case "player":
                player = level.player
                if not player:
                    player = Player(
                        "player", 1, Animations().player_animations, level.game.window
                    )

                x, y = 150 if not player else player.x, 150 if not player else player.y

                player.x, player.y = x, y
