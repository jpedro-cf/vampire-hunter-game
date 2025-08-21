from abc import ABC, abstractmethod

import pygame

from game.character_spritesheet import CharacterAnimations


class Entity(ABC):
    def __init__(
        self,
        name: str,
        animations: CharacterAnimations,
        surface: pygame.Surface,
    ):
        self.name = name

        self.x, self.y = 0, 0

        self.speed = 1
        self.health = 100
        self.damage = 10

        self.direction, self.state = "down", "idle"
        self.spritesheet: CharacterAnimations = animations
        self.surface = surface

        self.animation = self.spritesheet[self.state][self.direction].iter()
        self.image = self.animation.next()

    @abstractmethod
    def move(self):
        pass

    def update_animation(self):
        try:
            self.image = self.animation.next()
        except StopIteration:
            if self.state == "attack":
                self.state = "idle"
                self.animation = self.spritesheet[self.state][self.direction].iter()
            self.image = self.animation.next()

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
