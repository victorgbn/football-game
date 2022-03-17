from pygame import draw, sprite
from pygame.surface import Surface

from yellowcard import Yellowcard

class YellowcardFallEvent:

    def __init__(self, game) -> None:
        self.percent = int()
        self.percent_speed = 5 
        self.game = game
        # define sprite group of yellowcar
        self.all_yellowcards = sprite.Group()

    # add percent method
    def add_percent(self) -> None:
        self.percent += self.percent_speed / 100

    # push yellow card after load
    def attempt_fall(self) -> None:
        if self.is_full_loaded():
            self.yellowcard_fall()
            self.reset_percent()

    # push a yellow card
    def yellowcard_fall(self):
        self.all_yellowcards.add(Yellowcard(self))

    def is_full_loaded(self) -> bool:
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface: Surface) -> None:
        self.add_percent()
        self.attempt_fall()
        draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        draw.rect(surface, (122, 255, 119),
                  [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])
