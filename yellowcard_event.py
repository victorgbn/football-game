#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw, sprite
from pygame.surface import Surface

from yellowcard import Yellowcard


class YellowcardFallEvent:

    def __init__(self) -> None:
        self.percent = int()
        self.percent_speed = 5
        self.all_yellowcards = sprite.Group()

    def add_percent(self) -> None:
        self.percent += self.percent_speed / 100

    def attempt_fall(self) -> None:
        if self.is_full_loaded():
            self.yellowcard_fall()
            self.reset_percent()

    def yellowcard_fall(self):
        self.all_yellowcards.add(Yellowcard())

    def is_full_loaded(self) -> bool:
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface: Surface) -> None:
        self.add_percent()
        self.attempt_fall()
        draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        draw.rect(surface, (187, 11, 11),
                  [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])
