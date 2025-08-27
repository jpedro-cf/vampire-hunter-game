from typing import TypedDict
from game.spritesheet import SpriteSheetAnimation


class DirectionAnimations(TypedDict, total=False):
    left: SpriteSheetAnimation
    right: SpriteSheetAnimation
    up: SpriteSheetAnimation
    down: SpriteSheetAnimation


class CharacterAnimations(TypedDict, total=False):
    idle: DirectionAnimations
    walk: DirectionAnimations
    attack: DirectionAnimations
    hurt: DirectionAnimations
    death: DirectionAnimations


player_idle_path = "./assets/player/player_idle.png"
player_idle_size = 64

player_walk_path = "./assets/player/player_walk.png"
player_walk_size = 64

player_attack_path = "./assets/player/player_attack.png"
player_attack_size = 64

player_death_path = "./assets/player/player_death.png"
player_death_size = 64

player_hurt_path = "./assets/player/player_hurt.png"
player_hurt_size = 64

enemy_idle_path = "./assets/enemies/vampire_idle.png"
enemy_idle_size = 64

enemy_walk_path = "./assets/enemies/vampire_walk.png"
enemy_walk_size = 64

enemy_attack_path = "./assets/enemies/vampire_attack.png"
enemy_attack_size = 64

enemy_death_path = "./assets/enemies/vampire_death.png"
enemy_death_size = 64

enemy_hurt_path = "./assets/enemies/vampire_hurt.png"
enemy_hurt_size = 64


class Animations:
    def __init__(self):

        self.player_animations: CharacterAnimations = {
            "idle": {
                "down": SpriteSheetAnimation(
                    player_idle_path,
                    (0, player_idle_size * 0, player_idle_size, player_idle_size),
                    12,
                    1,
                    True,
                    12,
                ),
                "left": SpriteSheetAnimation(
                    player_idle_path,
                    (0, player_idle_size * 1, player_idle_size, player_idle_size),
                    12,
                    1,
                    True,
                    12,
                ),
                "right": SpriteSheetAnimation(
                    player_idle_path,
                    (0, player_idle_size * 2, player_idle_size, player_idle_size),
                    12,
                    1,
                    True,
                    12,
                ),
                "up": SpriteSheetAnimation(
                    player_idle_path,
                    (0, player_idle_size * 3, player_idle_size, player_idle_size),
                    4,
                    1,
                    True,
                    12,
                ),
            },
            "attack": {
                "down": SpriteSheetAnimation(
                    player_attack_path,
                    (
                        0,
                        player_attack_size * 0,
                        player_attack_size,
                        player_attack_size,
                    ),
                    8,
                    1,
                    False,
                    5,
                ),
                "left": SpriteSheetAnimation(
                    player_attack_path,
                    (
                        0,
                        player_attack_size * 1,
                        player_attack_size,
                        player_attack_size,
                    ),
                    8,
                    1,
                    False,
                    5,
                ),
                "right": SpriteSheetAnimation(
                    player_attack_path,
                    (
                        0,
                        player_attack_size * 2,
                        player_attack_size,
                        player_attack_size,
                    ),
                    8,
                    1,
                    False,
                    5,
                ),
                "up": SpriteSheetAnimation(
                    player_attack_path,
                    (
                        0,
                        player_attack_size * 3,
                        player_attack_size,
                        player_attack_size,
                    ),
                    8,
                    1,
                    False,
                    5,
                ),
            },
            "walk": {
                "down": SpriteSheetAnimation(
                    player_walk_path,
                    (0, player_walk_size * 0, player_walk_size, player_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
                "left": SpriteSheetAnimation(
                    player_walk_path,
                    (0, player_walk_size * 1, player_walk_size, player_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
                "right": SpriteSheetAnimation(
                    player_walk_path,
                    (0, player_walk_size * 2, player_walk_size, player_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
                "up": SpriteSheetAnimation(
                    player_walk_path,
                    (0, player_walk_size * 3, player_walk_size, player_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
            },
            "death": {
                "down": SpriteSheetAnimation(
                    player_death_path,
                    (
                        0,
                        player_death_size * 0,
                        player_death_size,
                        player_death_size,
                    ),
                    7,
                    1,
                    False,
                    12,
                ),
                "left": SpriteSheetAnimation(
                    player_death_path,
                    (
                        0,
                        player_death_size * 1,
                        player_death_size,
                        player_death_size,
                    ),
                    7,
                    1,
                    False,
                    12,
                ),
                "right": SpriteSheetAnimation(
                    player_death_path,
                    (
                        0,
                        player_death_size * 2,
                        player_death_size,
                        player_death_size,
                    ),
                    7,
                    1,
                    False,
                    12,
                ),
                "up": SpriteSheetAnimation(
                    player_death_path,
                    (
                        0,
                        player_death_size * 3,
                        player_death_size,
                        player_death_size,
                    ),
                    7,
                    1,
                    False,
                    12,
                ),
            },
            "hurt": {
                "down": SpriteSheetAnimation(
                    player_hurt_path,
                    (0, player_hurt_size * 0, player_hurt_size, player_hurt_size),
                    5,
                    1,
                    False,
                    8,
                ),
                "left": SpriteSheetAnimation(
                    player_hurt_path,
                    (0, player_hurt_size * 1, player_hurt_size, player_hurt_size),
                    5,
                    1,
                    False,
                    8,
                ),
                "right": SpriteSheetAnimation(
                    player_hurt_path,
                    (0, player_hurt_size * 2, player_hurt_size, player_hurt_size),
                    5,
                    1,
                    False,
                    8,
                ),
                "up": SpriteSheetAnimation(
                    player_hurt_path,
                    (0, player_hurt_size * 3, player_hurt_size, player_hurt_size),
                    5,
                    1,
                    False,
                    8,
                ),
            },
        }

        self.enemy_animations: CharacterAnimations = {
            "idle": {
                "down": SpriteSheetAnimation(
                    enemy_idle_path,
                    (0, enemy_idle_size * 0, enemy_idle_size, enemy_idle_size),
                    4,
                    1,
                    True,
                    12,
                ),
                "left": SpriteSheetAnimation(
                    enemy_idle_path,
                    (0, enemy_idle_size * 1, enemy_idle_size, enemy_idle_size),
                    4,
                    1,
                    True,
                    12,
                ),
                "right": SpriteSheetAnimation(
                    enemy_idle_path,
                    (0, enemy_idle_size * 2, enemy_idle_size, enemy_idle_size),
                    4,
                    1,
                    True,
                    12,
                ),
                "up": SpriteSheetAnimation(
                    enemy_idle_path,
                    (0, enemy_idle_size * 3, enemy_idle_size, enemy_idle_size),
                    4,
                    1,
                    True,
                    12,
                ),
            },
            "attack": {
                "down": SpriteSheetAnimation(
                    enemy_attack_path,
                    (0, enemy_attack_size * 0, enemy_attack_size, enemy_attack_size),
                    8,
                    1,
                    False,
                    8,
                ),
                "up": SpriteSheetAnimation(
                    enemy_attack_path,
                    (0, enemy_attack_size * 1, enemy_attack_size, enemy_attack_size),
                    8,
                    1,
                    False,
                    8,
                ),
                "left": SpriteSheetAnimation(
                    enemy_attack_path,
                    (0, enemy_attack_size * 2, enemy_attack_size, enemy_attack_size),
                    8,
                    1,
                    False,
                    8,
                ),
                "right": SpriteSheetAnimation(
                    enemy_attack_path,
                    (0, enemy_attack_size * 3, enemy_attack_size, enemy_attack_size),
                    8,
                    1,
                    False,
                    8,
                ),
            },
            "walk": {
                "down": SpriteSheetAnimation(
                    enemy_walk_path,
                    (0, enemy_walk_size * 0, enemy_walk_size, enemy_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
                "up": SpriteSheetAnimation(
                    enemy_walk_path,
                    (0, enemy_walk_size * 1, enemy_walk_size, enemy_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
                "left": SpriteSheetAnimation(
                    enemy_walk_path,
                    (0, enemy_walk_size * 2, enemy_walk_size, enemy_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
                "right": SpriteSheetAnimation(
                    enemy_walk_path,
                    (0, enemy_walk_size * 3, enemy_walk_size, enemy_walk_size),
                    6,
                    1,
                    True,
                    12,
                ),
            },
            "death": {
                "down": SpriteSheetAnimation(
                    enemy_death_path,
                    (0, enemy_death_size * 0, enemy_death_size, enemy_death_size),
                    11,
                    1,
                    False,
                    12,
                ),
                "up": SpriteSheetAnimation(
                    enemy_death_path,
                    (0, enemy_death_size * 1, enemy_death_size, enemy_death_size),
                    11,
                    1,
                    False,
                    12,
                ),
                "left": SpriteSheetAnimation(
                    enemy_death_path,
                    (0, enemy_death_size * 2, enemy_death_size, enemy_death_size),
                    11,
                    1,
                    False,
                    12,
                ),
                "right": SpriteSheetAnimation(
                    enemy_death_path,
                    (0, enemy_death_size * 3, enemy_death_size, enemy_death_size),
                    11,
                    1,
                    False,
                    12,
                ),
            },
            "hurt": {
                "down": SpriteSheetAnimation(
                    enemy_hurt_path,
                    (0, enemy_hurt_size * 0, enemy_hurt_size, enemy_hurt_size),
                    4,
                    1,
                    False,
                    6,
                ),
                "up": SpriteSheetAnimation(
                    enemy_hurt_path,
                    (0, enemy_hurt_size * 1, enemy_hurt_size, enemy_hurt_size),
                    4,
                    1,
                    False,
                    6,
                ),
                "left": SpriteSheetAnimation(
                    enemy_hurt_path,
                    (0, enemy_hurt_size * 2, enemy_hurt_size, enemy_hurt_size),
                    4,
                    1,
                    False,
                    6,
                ),
                "right": SpriteSheetAnimation(
                    enemy_hurt_path,
                    (0, enemy_hurt_size * 3, enemy_hurt_size, enemy_hurt_size),
                    4,
                    1,
                    False,
                    6,
                ),
            },
        }
