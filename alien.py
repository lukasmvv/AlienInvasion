import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """A class that defines an enemny alien"""

    def __init__(self, screen, settings):
        """A method that initializes an alien"""

        super(Alien, self).__init__()

        # Screen attributes
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Alien attributes
        self.path = settings.alien_path
        self.speed_increment = settings.alien_speed_increment
        self.max_speed = settings.alien_max_speed
        self.rotate = settings.alien_rotate
        self.scale = settings.alien_scale

        # Tilt settings
        self.tilt_max = settings.alien_tilt_max_angle
        self.tilt_angle = 0
        self.tilt_counter = 0
        self.tilt_increment = settings.alien_tilt_increment
        self.tilt_increasing = True
        self.tilt_frequency = settings.alien_tilt_frequency

        # Load the image, scale it and gets its rect
        self.image = pygame.image.load(self.path)
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        woh = self.image_width / self.image_height
        self.image_width = int(self.screen.get_width() / self.scale)
        self.image_height = int(self.image_width / woh)
        self.image = pygame.transform.smoothscale(self.image, (self.image_width, self.image_height))
        self.original_image = pygame.transform.rotate(self.image, self.rotate)
        self.rect = self.image.get_rect()

        # Start each new alien aa random position on the far right of screen
        self.rect.left = self.screen_rect.right
        self.rect.centery = random.randint(self.image_height/2, (self.screen_rect.bottom-self.image_height/2)+1)

        # Movement
        self.delta_x = 0
        self.delta_y = 0

    def blitme(self):
        """Draw the alien to screen"""

        center_rect = pygame.Rect(0, 0, 10, 10)
        center_rect.centerx = self.rect.centerx
        center_rect.centery = self.rect.centery
        pygame.draw.rect(self.screen, (60, 60, 60), center_rect)
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """Update alien position and tilt angle on screen"""

        # Incrementing delta x
        self.delta_x += self.speed_increment

        # Checking if delta x is greater than max delta x
        if int(self.delta_x) > self.max_speed:
            self.rect.centerx -= int(self.delta_x)
            self.delta_x = 0

        # Updating tilt angle
        last_angle = self.tilt_angle
        increment = 0
        center = self.rect.center

        # Checking angle ranges and increasing tilt angle
        if self.rect.centerx % self.tilt_frequency == 0:
            if last_angle == self.tilt_max:
                increment = -self.tilt_increment
                self.tilt_increasing = False
            elif last_angle == -self.tilt_max:
                increment = self.tilt_increment
                self.tilt_increasing = True
            elif self.tilt_increasing:
                increment = self.tilt_increment
            elif not self.tilt_increasing:
                increment = -self.tilt_increment

            # Incrementing tilt angle
            self.tilt_angle += increment

            # Rotating original image
            self.image = pygame.transform.rotate(self.original_image, self.tilt_angle)  # never rotate the image being displayed. always rotate original image

            # Setting new rect and setting its center
            self.rect = self.image.get_rect()
            self.rect.center = center

