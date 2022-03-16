import pygame

class SoundManager:
    
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'shoot': pygame.mixer.Sound("assets/sounds/shoot.ogg"),
            'yellowcard': pygame.mixer.Sound("assets/sounds/yellowcard.ogg")
        }
    
    def play(self, name) -> None:
        self.sounds[name].play()