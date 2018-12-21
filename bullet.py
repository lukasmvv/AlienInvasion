import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for a bullet fired from player ship"""

    def __init__(self, screen, settings, ship):
        """Initialize method for bullet"""

        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rectangle at 0,0 then set correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.left = ship.rect.right
        self.rect.centery = ship.rect.centery
        self.color = settings.bullet_colour
        self.speed_factor = settings.bullet_speed_increment
        self.max_speed = settings.bullet_max_speed

        self.delta_x = 0

    def update_position(self):
        """Update bullet position"""

        # Incrementing delta x
        self.delta_x += self.speed_factor

        # Checking of delta x is greater than max delta x
        if int(self.delta_x) >= self.max_speed:
            self.rect.centerx += int(self.delta_x)
            self.delta_x = 0

    def draw_bullet(self):
        """Draw bullet to screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)