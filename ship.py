import pygame


class Ship():
    """This class contains all info and methods relating to the player ship"""

    def __init__(self, screen, settings):
        """Initializes the ship on the given screen"""

        # Screen attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Ship attributes
        self.ship_path = settings.ship_image_path
        self.ship_scale = settings.ship_scale
        self.ship_starting_scale_x = settings.ship_start_x
        self.lives = settings.ship_lives
        self.hit = False

        # Load the image, scale it and gets its rect
        self.image = pygame.image.load(self.ship_path)
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        woh = self.image_width/self.image_height
        self.image_width = int(self.screen.get_width()/self.ship_scale)
        self.image_height = int(self.image_width/woh)
        self.image = pygame.transform.smoothscale(self.image, (self.image_width, self.image_height))
        self.image = pygame.transform.rotate(self.image, settings.ship_rotate)
        self.rect = self.image.get_rect()

        # Start each new ship at centre vertically and 30% from left screen side
        self.rect.centerx = int(self.screen_rect.right*self.ship_starting_scale_x)
        self.rect.centery = self.screen_rect.centery

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Movement settings
        self.increments = settings.ship_speed_increment
        self.max_speed = settings.ship_max_speed
        self.delta_r = 0
        self.delta_l = 0
        self.delta_u = 0
        self.delta_d = 0

    def blitme(self):
        """Draw the ship to screen"""

        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """Update ship position based on movement"""

        # Moving ship right and checking right border
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Adding increments to delta_r
            self.delta_r += self.increments
            # Adding delta_r to centrex. WIll only happen when int(delta_r) > 0
            self.rect.centerx += int(self.delta_r)
            # Once delta_r has been added, make it 0 again
            if int(self.delta_r) > 0:
                self.delta_r = 0
        else:
            self.delta_r = 0

        # Moving ship left and checking left border
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # Adding increments to delta_l
            self.delta_l += self.increments
            # Subtracting delta_l from centrex. WIll only happen when int(delta_l) > 0
            self.rect.centerx -= int(self.delta_l)
            # Once delta_l has been subtracted, make it 0 again
            if int(self.delta_l) > 0:
                self.delta_l = 0
        else:
            self.delta_l = 0

        # Moving ship up and checking top border
        if self.moving_up and self.rect.top > self.screen_rect.top:
            # Adding increments to delta_u
            self.delta_u += self.increments
            # Adding delta_u to centrey. WIll only happen when int(delta_u) > 0
            self.rect.centery -= int(self.delta_u)
            # Once delta_u has been added, make it 0 again
            if int(self.delta_u) > 0:
                self.delta_u = 0
        else:
            self.delta_u = 0

        # Moving ship down and checking bottom border
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # Adding increments to delta_d
            self.delta_d += self.increments
            # Subtracting delta_d from centrey. WIll only happen when int(delta_d) > 0
            self.rect.centery += int(self.delta_d)
            # Once delta_d has been subtracted, make it 0 again
            if int(self.delta_d) > 0:
                self.delta_d = 0
        else:
            self.delta_d = 0
