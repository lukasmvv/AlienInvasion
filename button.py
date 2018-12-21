import pygame.ftfont


class Button():
    """Class for buttons"""

    def __init__(self, settings, screen, message):
        """Initiliaze button"""

        # Screen attributes
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Button attributes
        self.height = settings.button_height
        self.width = settings.button_width
        self.color = settings.button_color
        self.text_color = settings.button_text_color
        self.font = settings.button_font

        # Building button rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Rendering button  text as image for python to display to screen
        self.message_image = self.font.render(message, True, self.text_color, self.color)  # True turns aliasing on
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        """Method which draws button"""

        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)