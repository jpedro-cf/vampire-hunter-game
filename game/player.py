import pygame
from game.entity import Entity


class Player(Entity):
    def __init__(self, name, animations, surface, x=0, y=0):
        super().__init__(name, animations, surface)
        self.x, self.y = x, y

    def move(self, keys: pygame.key.ScancodeWrapper):
        moving = False
        prev_state, prev_direction = self.state, self.direction

        if keys[pygame.K_e]:
            self.state = "attack"
            moving = True
            self.attack()

        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "up"
            moving = True
        elif keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "down"
            moving = True
        elif keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "left"
            moving = True
        elif keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "right"
            moving = True

        if not moving and self.state != "attack":
            self.state = "idle"
        elif moving and self.state != "attack":
            self.state = "walk"

        # Only reset animation if the state or direction changed
        if (self.state, self.direction) != (prev_state, prev_direction):
            self.animation = self.spritesheet[self.state][self.direction].iter()

    def attack(self):
        pass
