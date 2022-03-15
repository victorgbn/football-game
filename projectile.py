#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image, sprite, transform


class Projectile(sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 5
        self.image = image.load('assets/projectile.png')
        self.image = transform.scale(self.image, (50, 50))
        self.origin_image = self.image
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

    def move(self) -> None:
        self.rect.x += self.velocity
        self.rotate()
        for referee in self.player.game.check_collision(self, self.player.game.all_referees):
            self.remove()
            referee.damage(self.player.attack)
        if self.rect.x > 1080:
            self.remove()

    def remove(self) -> None:
        self.player.all_projectiles.remove(self)

    def rotate(self) -> None:
        self.angle += 12
        self.image = transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
