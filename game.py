#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

from pygame import K_LEFT, K_RIGHT
from pygame.sprite import Group, Sprite, spritecollide

from yellowcard_event import YellowcardFallEvent
from referee import Referee
from player import Player


class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_players = Group()
        self.all_players.add(self.player)
        self.yellowcard_event = YellowcardFallEvent()
        self.all_referees = Group()
        self.pressed = dict()

    def check_collision(self, sprite: Sprite, group: Group) -> List[Sprite]:
        return spritecollide(sprite, group, False)

    def game_over(self) -> None:
        self.all_referees = Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def spawn_referee(self) -> None:
        referee = Referee(self)
        self.all_referees.add(referee)

    def start(self) -> None:
        self.is_playing = True
        self.spawn_referee()
        self.spawn_referee()

    def update(self, screen) -> None:
        # Application du joueur sur la surface
        screen.blit(self.player.image, self.player.rect)

        # Application de la barre de vie du joueur
        self.player.update_health_bar(screen)

        self.yellowcard_event.update_bar(screen)

        # Déplacement des projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        # Déplacement des montres
        for referee in self.all_referees:
            referee.forward()
            referee.update_health_bar(screen)
        for yellowcard in self.yellowcard_event.all_yellowcards:
            yellowcard.fall()

        # Application des projectiles sur la surface
        self.player.all_projectiles.draw(screen)
        # Application des monstres sur la surface
        self.all_referees.draw(screen)
        # Application des comètes sur la surface
        self.yellowcard_event.all_yellowcards.draw(screen)

        # Déplacement du joueur
        if self.pressed.get(K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
