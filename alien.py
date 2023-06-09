import pygame
from pygame.sprite import Sprite
from pygame import mixer

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game, bullets):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullets = bullets

        # Load the alien image and set its rect attribure.
        self.image = pygame.image.load(ai_game.resource_path("assets/images/alien.bmp"))
        self.rect = self.image.get_rect()

        # Start each new alien newr the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

        # Initiate mixer and Load The sound of hit
        mixer.init()
        self.hit_sound = mixer.Sound(ai_game.resource_path("assets/sounds/explosion.wav"))


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right and left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


