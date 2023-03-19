import pygame
from pygame.sprite import Sprite
from pygame import mixer
import os
import random


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        # Make an instance of ai_game
        self.ai_game = ai_game

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def play_sound(self):
        """Play a sound when the ship collide with enemy and return sound length."""
        self.ship_sound = mixer.Sound(self._choose_a_random_sound_file("sounds/ship_hit_sounds"))
        self.ship_sound.play()
        # Return the time duration of the sound.
        return self.ship_sound.get_length()


    def _choose_a_random_sound_file(self, sound_dir):
        """This method choose a file randomly from a directory."""
        dir_path = sound_dir
        files = os.listdir(dir_path)
        file_name = random.choice(files)
        full_path = os.path.join(dir_path, file_name)
        return full_path


