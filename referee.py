#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from pygame import draw, image
from pygame.sprite import Sprite
from pygame.surface import Surface


class Referee(Sprite):

    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = image.load('assets/referee.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.recycle()

    def update_health_bar(self, surface: Surface) -> None:
        draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self) -> None:
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

    def recycle(self) -> None:
        self.rect.x = 1000 + random.randint(0, 300)
        self.health = self.max_health
        self.velocity = random.randint(1, 3)
