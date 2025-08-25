from typing import Dict
import pygame
from game.character import Character
from game.character_factory import CharacterFactory
from game.character_mediator import CharacterMediator
from game.object import Object


class Level:
    def __init__(self, name: str, level: int, surface: pygame.Surface):
        self.name = name
        self.level = level
        self.enemies: Dict[str, Character] = {}
        self.loots: Dict[str, Object] = {}
        self.player = None
        self.surface = surface

        self.spawn_delay = 30 * 1000
        self.last_spawn_time = 0
        self.enemies_per_time = 2

        self.loots_delay = 15 * 1000
        self.last_loot_time = 0

        self.player = CharacterFactory.get_entity("player", self.level, self.surface)

        for _ in range(self.enemies_per_time * self.level):
            enemy = CharacterFactory.get_entity("enemy", self.level, self.surface)
            enemy.player = self.player
            self.enemies[enemy.name] = enemy

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.player:
                self.player = CharacterFactory.get_entity(
                    "player", self.level, self.surface
                )

            if not self.enemies:
                self.spawn_enemies()

            self.surface.fill((0, 0, 0))

            current_time = pygame.time.get_ticks()

            if current_time - self.last_spawn_time >= self.spawn_delay:
                self.spawn_enemies()
                self.last_spawn_time = current_time

            if current_time - self.last_loot_time >= self.loots_delay:
                self.spawn_loot()
                self.last_loot_time = current_time

            for key in list(self.enemies.keys()):
                enemy = self.enemies[key]

                CharacterMediator.verify_attack(self.player, enemy)
                CharacterMediator.verify_attack(enemy, self.player)

                enemy.move()
                enemy.update_animation()
                enemy.draw()

                if enemy.health <= 0 and enemy.animation.i >= len(
                    enemy.animation.images
                ):
                    self.enemies.pop(key)
                if self.player.health <= 0 and self.player.animation.i >= len(
                    self.player.animation.images
                ):
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
                break

            self.player.move()
            self.player.update_animation()
            self.player.draw()

            pygame.display.flip()

            clock.tick(60)
        pygame.quit()

    def spawn_enemies(self):
        for _ in range(self.enemies_per_time * self.level):
            enemy = CharacterFactory.get_entity("enemy", self.level, self.surface)
            enemy.player = self.player
            self.enemies[enemy.name] = enemy

    def spawn_loot(self):
        loot = CharacterFactory.get_entity("loot", self.spawn_delay, self.surface)
        self.loots[loot.name] = loot
