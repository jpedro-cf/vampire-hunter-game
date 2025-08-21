import pygame

from game.character_spritesheet import Animations
from game.const import SCREEN_HEIGHT, SCREEN_WIDTH
from game.level import Level
from game.menu import Menu
from game.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.player = Player("player", 1, Animations().player_animations, self.window)

    def run(self):
        level = Level("level1", 1, self)
        running = True
        while running:
            # menu = Menu(self.window).run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill((0, 0, 0))

            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.player.update_animation()
            self.player.draw()

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
