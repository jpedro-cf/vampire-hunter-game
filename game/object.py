from abc import ABC, abstractmethod
from pygame import Surface
import pygame
from game.character import Character


class Object(ABC):
    def __init__(self, name: str, type: str, surface: Surface, image: str, x, y):
        self.name = name
        self.type = type

        self.surface = surface
        self.image = pygame.image.load(image).convert_alpha()

        self.x, self.y = x, y

        self.target: Character = None

        self.picked_at: int = None
        self.duration: int = 5 * 1000

    @abstractmethod
    def apply_effect(self, target: Character):
        self.picked_at = pygame.time.get_ticks()

    @abstractmethod
    def remove_effect(self):
        pass

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def update(self):
        if self.picked_at is not None:
            elapsed = pygame.time.get_ticks() - self.picked_at
            if elapsed >= self.duration:
                self.remove_effect()
                self.picked_at = None
                return True
        return False
