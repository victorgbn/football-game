from pygame import draw, image, sprite
from pygame.surface import Surface

from projectile import Projectile

# Create PlayerType
class Player(sprite.Sprite):

    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 34
        self.velocity = 5
        self.all_projectiles = sprite.Group()
        self.image = image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    # Added Player Damages
    def damage(self, amount: int) -> None:
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    # Allow player to lauch projectiles
    def launch_projectile(self) -> None:
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play('shoot')

    # Player move to left
    def move_left(self) -> None:
        self.rect.x -= self.velocity

    # Player move to right
    def move_right(self) -> None:
        if not self.game.check_collision(self, self.game.all_referees):
            self.rect.x += self.velocity

    # Player Health Bar
    def update_health_bar(self, surface: Surface) -> None:
        draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y + - 5, self.max_health, 7])
        draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y + - 5, self.health, 7])
