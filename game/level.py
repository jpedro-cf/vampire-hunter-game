from typing import Dict
import pygame
from game.character import Character
from game.character_factory import CharacterFactory
from game.character_mediator import CharacterMediator


class Level:
    def __init__(self, name: str, level: int, surface: pygame.Surface):
        self.name = name
        self.level = level
        self.enemies: Dict[int, Character] = {}
        self.player = None
        self.surface = surface

        self.spawn_delay = 10 * 1000
        self.last_spawn_time = 0
        self.enemies_per_time = 2

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
                    "player", self.level, self.surface, None
                )

            self.surface.fill((0, 0, 0))

            keys = pygame.key.get_pressed()

            self.player.move()
            self.player.update_animation()
            self.player.draw()

            current_time = pygame.time.get_ticks()

            if current_time - self.last_spawn_time >= self.spawn_delay:
                # self.spawn_enemies()
                self.last_spawn_time = current_time

            for key in list(self.enemies.keys()):
                enemy = self.enemies[key]
                enemy.move()
                enemy.draw()
                enemy.update_animation()

                CharacterMediator.verify_attack(self.player, enemy)
                CharacterMediator.verify_attack(enemy, self.player)

                if enemy.health <= 0 and enemy.animation.i >= len(
                    enemy.animation.images
                ):
                    self.enemies.pop(key)

            pygame.display.flip()

            clock.tick(60)
        pygame.quit()

    def spawn_enemies(self):
        for i in range(self.enemies_per_time * self.level):
            enemy = CharacterFactory.get_entity(
                "enemy", self.level, self.surface, self.player
            )
            self.enemies[enemy.name] = enemy
