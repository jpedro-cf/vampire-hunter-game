from tkinter.font import Font
import pygame

from game.const import SCREEN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(
            "./assets/backgrounds/terrace.png"
        ).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.options = ("START", "EXIT")

    def run(self):
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(
                50, "Vampire Hunter", (255, 128, 0), ((SCREEN_WIDTH / 2), 70)
            )

            for i, option in enumerate(self.options):
                text_position = ((SCREEN_WIDTH / 2), 200 + 25 * i)
                if i == menu_option:
                    self.menu_text(20, option, (255, 255, 128), text_position)
                else:
                    self.menu_text(20, option, (255, 255, 255), text_position)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type != pygame.KEYDOWN:
                    continue

                if event.key == pygame.K_DOWN:
                    if menu_option < len(self.options) - 1:
                        menu_option += 1
                    else:
                        menu_option = 0
                if event.key == pygame.K_UP:
                    if menu_option > 0:
                        menu_option -= 1
                    else:
                        menu_option = len(self.options) - 1

                if event.key == pygame.K_RETURN:
                    return self.options[menu_option]

    def menu_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color
        ).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
