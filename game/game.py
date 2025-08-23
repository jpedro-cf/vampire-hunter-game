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
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        level = Level("level1", 1, self.window)
        while running:
            # menu = Menu(self.window).run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            level.run()

            self.clock.tick(60)

        pygame.quit()
