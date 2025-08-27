import pygame
from game.character import Character
from game.const import SCREEN_HEIGHT, SCREEN_WIDTH


class Player(Character):
    def __init__(self, name, animations, surface, x, y, play_area: pygame.Rect):
        super().__init__(name, animations, surface, play_area)
        self.x, self.y = x, y
        self.speed = 2
        self.damage = 35
        self.attack_range = 30

        self.kills = 0

        self.width, self.height = 64, 64

    def move(self):
        keys = pygame.key.get_pressed()
        moving = False
        prev_state, prev_direction = self.state, self.direction

        direction = self.direction
        if keys[pygame.K_w]:
            self.y = max(self.play_area.top, self.y - self.speed)
            direction = "up"
            moving = True
        elif keys[pygame.K_s]:
            self.y = min(self.play_area.bottom - self.height, self.y + self.speed)
            direction = "down"
            moving = True
        elif keys[pygame.K_a]:
            self.x = max(self.play_area.left, self.x - self.speed)
            direction = "left"
            moving = True
        elif keys[pygame.K_d]:
            self.x = min(self.play_area.right - self.width, self.x + self.speed)
            direction = "right"
            moving = True

        if self.state in ["hurt", "death"]:
            return

        if keys[pygame.K_e]:
            self.state = "attack"
            moving = True
            self.attack()

        if not moving and self.state != "attack":
            self.state = "idle"
        elif moving and self.state != "attack":
            self.state = "walk"

        if self.state != "attack":
            self.direction = direction

        # Only reset animation if the state or direction changed
        if (self.state, self.direction) != (prev_state, prev_direction):
            self.animation = self.spritesheet[self.state][self.direction].iter()

    def attack(self):
        pass

    def hurt(self):
        return super().hurt()

    def die(self):
        return super().die()
