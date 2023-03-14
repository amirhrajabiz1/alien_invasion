import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A class to represent an explosion animation."""

    def __init__(self, ai_game, center):
        """Initialize the explosion animation."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Define the number of small sprites in horizontal and vertical.
        self.num_horizontal_small_sprites = 13
        self.num_vertical_small_sprites = 1

        self.big_image = pygame.image.load("images/explosion.png")

        # Define the size of each small sprites.
        self.width_sprite = self.big_image.get_width() // self.num_horizontal_small_sprites
        self.height_sprite = self.big_image.get_height() // self.num_vertical_small_sprites

        self.rect = self.big_image.get_rect()
        self.rect.center = center

        # Initiate the frames variable
        self.frames = []
        

        # This loop store all small sprites in "sprites" list.
        for row in range(self.num_vertical_small_sprites):
            for col in range(self.num_horizontal_small_sprites):
                x = col * self.width_sprite
                y = row * self.height_sprite
                self.sprite = self.big_image.subsurface(
                    pygame.Rect(x, y, self.width_sprite, self.height_sprite)
                )
                self.frames.append(self.sprite)

        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.animation_speed = self.settings.explosion_long
        self.last_update = pygame.time.get_ticks()

    def update(self):
        """Update the explosion animation."""
        # Get the time of now
        now = pygame.time.get_ticks()

        # In this if statement we adjust the speed of show the explosion animation
        # and show the frames of animation and adjust the position of the frame.
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame == len(self.frames):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    


