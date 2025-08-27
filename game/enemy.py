import math
import random
import pygame
from game.character import Character
from game.player import Player


class Enemy(Character):
    def __init__(self, name, animations, surface, play_area):
        super().__init__(name, animations, surface, play_area)
        self.player = None

        self.attack_cooldown = 3000
        self.last_attack_time = 0

    def move(self):
        if self.state in ["attack", "hurt", "death"]:
            return

        prev_state, prev_direction = self.state, self.direction

        player_x, player_y = self.player.x, self.player.y
        x, y = self.x, self.y

        pos_x, pos_y = player_x - x, player_y - y

        magnitude = (pos_x**2 + pos_y**2) ** 0.5
        dx = pos_x / max(magnitude, 1) * self.speed
        dy = pos_y / max(magnitude, 1) * self.speed

        dx += (random.random() - 0.8) * 0.8
        dy += (random.random() - 0.8) * 0.8

        self.x += dx
        self.y += dy

        self.state = "walk"
        if abs(pos_x) > abs(pos_y):
            self.direction = "right" if pos_x > 0 else "left"
        else:
            self.direction = "down" if pos_y > 0 else "up"

        dx = player_x - self.x
        dy = player_y - self.y
        distance = math.hypot(dx, dy)

        attack_range = 50

        if distance <= attack_range:
            self.attack()

        if (self.state, self.direction) != (prev_state, prev_direction):
            self.animation = self.spritesheet[self.state][self.direction].iter()

    def attack(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            self.state = "attack"
            self.last_attack_time = current_time

    def hurt(self):
        return super().hurt()

    def die(self):
        return super().die()
