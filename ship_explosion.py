import pygame


class Explosion:
    """A class to represent an explosion animation of the ship."""

    def __init__(self, ai_game, centerx, centery):
        """Initialize the explosion animation."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Define the number of small sprites in horizontal and vertical.
        self.num_horizontal_small_sprites = 3
        self.num_vertical_small_sprites = 3

        self.big_image = pygame.image.load(ai_game.resource_path("assets/images/explosion_atlas.png"))

        # Define the size of each small sprites.
        self.width_sprite = (
            self.big_image.get_width() // self.num_horizontal_small_sprites
        )
        self.height_sprite = (
            self.big_image.get_height() // self.num_vertical_small_sprites
        )

        self.rect = self.big_image.get_rect()

        # define how much the explosion animation should go down.
        self.adjust_explosion_animation = 18

        self.rect.centerx = centerx
        self.rect.centery = centery + self.adjust_explosion_animation

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

                # Resize the sprite with ship size.
                self.resized_sprite = pygame.transform.scale(
                    self.sprite,
                    (ai_game.ship.rect.width // 2.8, ai_game.ship.rect.height // 1.6),
                )

                self.frames.append(self.resized_sprite)

        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.animation_speed = self.settings.explosion_long
        self.last_update = pygame.time.get_ticks()

        # Initial the ai_game instance.
        self.ai_game = ai_game

    def update(self, centerx, centery):
        """Update the explosion animation."""

        # Update the center of explosion.
        self.rect.centerx = centerx
        self.rect.centery = centery + self.adjust_explosion_animation

        # Get the time of now
        now = pygame.time.get_ticks()

        # In this if statement we adjust the speed of show the explosion animation
        # and show the frames of animation and adjust the position of the frame.
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame == len(self.frames):
                self.current_frame = 0
            else:
                center = self.rect.center
                self.image = self.frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.centerx = centerx
                self.rect.centery = centery + self.adjust_explosion_animation

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
