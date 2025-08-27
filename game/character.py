from abc import ABC, abstractmethod

import pygame

from game.character_spritesheet import CharacterAnimations


class Character(ABC):
    def __init__(
        self,
        name: str,
        animations: CharacterAnimations,
        surface: pygame.Surface,
        play_area: pygame.Rect,
    ):
        self.name = name

        self.x, self.y = 0, 0
        self.play_area = play_area

        self.speed = 1
        self.health = 100
        self.damage = 10
        self.attack_range = 50

        self.direction, self.state = "down", "idle"
        self.spritesheet: CharacterAnimations = animations
        self.surface = surface

        self.animation = self.spritesheet[self.state][self.direction].iter()
        self.image = self.animation.next()

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def die(self):
        self.state = "death"
        self.animation = self.spritesheet[self.state][self.direction].iter()

    @abstractmethod
    def hurt(self):
        if self.state == "death":
            return

        self.state = "hurt"
        self.animation = self.spritesheet[self.state][self.direction].iter()

    def update_animation(self):
        try:
            self.image = self.animation.next()
        except StopIteration:
            if self.state in ["attack", "hurt", "death"]:
                self.state = "idle"
                self.animation = self.spritesheet[self.state][self.direction].iter()
            self.image = self.animation.next()

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
