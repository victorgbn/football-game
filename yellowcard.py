from random import randint

from pygame import image, sprite


class Yellowcard(sprite.Sprite):

    def __init__(self, yellowcard_event):
        super().__init__()
        self.image = image.load('assets/yellowcard.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, 800)
        self.rect.y = - randint(0, 800)
        self.velocity = randint(1, 3)
        self.yellowcard_event = yellowcard_event

    def remove(self):
        self.yellowcard_event.all_yellowcards.remove(self)
        self.yellowcard_event.game.sound_manager.play('yellowcard')

    def fall(self):
        self.rect.y += self.velocity
        # touch the ground
        if self.rect.y >= 500:
           self.remove()
        
        # if yellowcard touch player
        if self.yellowcard_event.game.check_collision(self, self.yellowcard_event.game.all_players):
            self.remove()
            self.yellowcard_event.game.player.damage(20)
