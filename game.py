from typing import List

import pygame
from pygame import K_LEFT, K_RIGHT
from pygame.sprite import Group, Sprite, spritecollide

from yellowcard_event import YellowcardFallEvent
from referee import Referee
from player import Player
from sounds import SoundManager

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_players = Group()
        self.all_players.add(self.player)
        self.yellowcard_event = YellowcardFallEvent(self)
        self.all_referees = Group()
        self.pressed = dict()
        self.score = 0
        self.font = pygame.font.Font("assets/font.ttf", 40)
        self.sound_manager = SoundManager()

    def check_collision(self, sprite: Sprite, group: Group) -> List[Sprite]:
        return spritecollide(sprite, group, False)

    def game_over(self) -> None:
        self.all_referees = Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def spawn_referee(self) -> None:
        referee = Referee(self)
        self.all_referees.add(referee)

    def start(self) -> None:
        self.is_playing = True
        self.spawn_referee()
        self.spawn_referee()

    def update(self, screen) -> None:
        # Added player in screen
        screen.blit(self.player.image, self.player.rect)

        # Added health bar in player
        self.player.update_health_bar(screen)

        self.yellowcard_event.update_bar(screen)

        ## Added score
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (510, 400))

        # Move Projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        # Move Referees
        for referee in self.all_referees:
            referee.forward()
            referee.update_health_bar(screen)
        # Move Yellow card
        for yellowcard in self.yellowcard_event.all_yellowcards:
            yellowcard.fall()

        # Added in scren
        self.player.all_projectiles.draw(screen)
        self.all_referees.draw(screen)
        self.yellowcard_event.all_yellowcards.draw(screen)

        # Move player
        if self.pressed.get(K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
