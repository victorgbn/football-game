#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw, image, sprite
from pygame.surface import Surface

from projectile import Projectile

# Create PlayerType
class Player(sprite.Sprite):

    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = sprite.Group()
        self.image = image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount: int) -> None:
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self) -> None:
        # Init projectile
        self.all_projectiles.add(Projectile(self))

    def move_left(self) -> None:
        self.rect.x -= self.velocity

    def move_right(self) -> None:
        if not self.game.check_collision(self, self.game.all_referees):
            self.rect.x += self.velocity

    def update_health_bar(self, surface: Surface) -> None:
        draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
