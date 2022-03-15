#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from pygame import image, sprite


class Yellowcard(sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = image.load('assets/yellowcard.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, 800)
        self.rect.y = - randint(0, 800)
        self.velocity = randint(1, 3)

    def fall(self):
        self.rect.y += self.velocity
