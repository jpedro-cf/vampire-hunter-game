import pygame

from game.character_spritesheet import Animations
from game.const import SCREEN_HEIGHT, SCREEN_WIDTH
from game.level import Level
from game.menu import DeathMenu, Menu, WinMenu
from game.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            menu_option = Menu(self.window).run()

            if menu_option == "EXIT":
                running = False
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            option = "TRY AGAIN"
            death_menu = DeathMenu(self.window)
            win_menu = WinMenu(self.window)
            while option != "EXIT":
                level = Level("level1", 1, self.window)
                won = level.run()

                option = win_menu.run() if won else death_menu.run()

            self.clock.tick(60)

        pygame.quit()
