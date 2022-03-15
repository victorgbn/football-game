from math import ceil
import pygame

from game import Game

pygame.init()

# Create Window game
pygame.display.set_caption("Stadium Game")
screen = pygame.display.set_mode(size=(1080, 720))

## Init background
background = pygame.image.load('assets/bg.jpg')

## Added player button
play_button = pygame.transform.scale(pygame.image.load('assets/button.jpg'), (400, 500))
play_button_rect = play_button.get_rect()
play_button_rect.x = ceil(screen.get_width() / 3)
play_button_rect.y = ceil(screen.get_height() / 3.5)

# Init a game
game = Game()
game_is_running = True

while game_is_running:

    ## Added background
    screen.blit(background, (-650, -300))

    # Check if game is playing
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)

    ## update screen show
    pygame.display.flip()

    # Events
    for event in pygame.event.get():
        ## If close window
        if event.type == pygame.QUIT:
            game_is_running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            ## Press SpaceKey
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
