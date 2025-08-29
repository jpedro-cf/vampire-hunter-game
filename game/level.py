from typing import Dict
import pygame
from game.character import Character
from game.character_factory import CharacterFactory
from game.character_mediator import CharacterMediator
from game.const import C_WHITE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.object import Object


class Level:
    def __init__(self, name: str, level: int, surface: pygame.Surface):
        self.levels = {0: 1, 10: 2, 25: 3, 50: 4, 100: 5}

        self.name = name
        self.level = level
        self.enemies: Dict[str, Character] = {}
        self.loots: Dict[str, Object] = {}
        self.player = None
        self.surface = surface

        self.spawn_delay = 30 * 1000
        self.last_spawn_time = self.spawn_delay * 2
        self.enemies_per_time = 2

        self.loots_delay = 10 * 1000
        self.last_loot_time = 0

        self.play_area = pygame.Rect(100, 225, 600, 360)

        self.player = CharacterFactory.get_entity(
            "player", self.level, self.surface, self.play_area
        )
        self.image = pygame.image.load("./assets/backgrounds/terrace.png").convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.enemies:
                self.spawn_enemies()

            self.surface.blit(self.image, (0, 0))

            current_time = pygame.time.get_ticks()

            if current_time - self.last_spawn_time >= self.spawn_delay:
                self.spawn_enemies()
                self.last_spawn_time = current_time

            if current_time - self.last_loot_time >= self.loots_delay:
                self.spawn_loot()
                self.last_loot_time = current_time

            for key in list(self.enemies.keys()):
                enemy = self.enemies[key]

                if not self.player:
                    break

                CharacterMediator.verify_attack(self.player, enemy)
                CharacterMediator.verify_attack(enemy, self.player)

                enemy.move()
                enemy.update_animation()
                enemy.draw()

                if enemy.health <= 0 and enemy.animation.i >= len(
                    enemy.animation.images
                ):
                    self.enemies.pop(key)
                    self.player.kills += 1

                if self.player.health <= 0 and self.player.animation.i >= len(
                    self.player.animation.images
                ):
                    self.player.draw()
                    self.player = None

            for key in list(self.loots.keys()):
                loot = self.loots[key]

                if loot.picked_at is not None:
                    updated = loot.update()
                    if updated:
                        self.loots.pop(loot.name)
                    continue

                loot.draw()

                CharacterMediator.verify_collision(self.player, loot)

            if not self.player:
                return False

            if self.player.kills in self.levels:
                self.level = self.levels[self.player.kills]

            if self.player.kills >= 150:
                return True

            self.player.move()
            self.player.update_animation()
            self.player.draw()

            self.level_text(
                14,
                f"Level {self.level}",
                C_WHITE,
                (10, 5),
            )

            self.level_text(
                14,
                f"Kills: {self.player.kills}/150",
                C_WHITE,
                (10, SCREEN_HEIGHT - 20),
            )
            self.level_text(
                14,
                f"Vida: {self.player.health}",
                C_WHITE,
                (10, SCREEN_HEIGHT - 40),
            )
            self.level_text(
                14,
                f"Dano: {self.player.damage}",
                C_WHITE,
                (10, SCREEN_HEIGHT - 60),
            )
            self.level_text(
                14,
                f"Velocidade: {self.player.speed}",
                C_WHITE,
                (10, SCREEN_HEIGHT - 80),
            )

            pygame.display.flip()

            clock.tick(60)
        pygame.quit()

    def spawn_enemies(self):
        for _ in range(self.enemies_per_time * self.level):
            enemy = CharacterFactory.get_entity(
                "enemy", self.level, self.surface, self.play_area
            )
            enemy.player = self.player
            self.enemies[enemy.name] = enemy

    def spawn_loot(self):
        loot = CharacterFactory.get_entity(
            "loot", self.spawn_delay, self.surface, self.play_area
        )
        self.loots[loot.name] = loot

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color
        ).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.surface.blit(source=text_surf, dest=text_rect)
