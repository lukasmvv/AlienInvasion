import pygame.font


class Scoreboard():
        """"A class to display score and lives and high score"""

        def __init__(self, stats, screen, settings, player):
            """Initialize"""

            # Screen attributes
            self.screen = screen
            self.screen_rect = self.screen.get_rect()

            # Scores
            self.high_score = 0
            self.score = 0
            self.lives = player.lives

            # Display
            self.font = settings.scoreboard_font
            self.color = settings.scoreboard_text_color

            # Score image
            self.score_image = self.font.render("", True, self.color, self.color)
            self.score_rect = self.score_image.get_rect()
            self.prep_score(settings, stats)

            # High score image
            self.high_score_image = self.font.render("", True, self.color, self.color)
            self.high_score_rect = self.high_score_image.get_rect()
            self.prep_high_score(settings, stats)

            # Prep ship lives
            self.lives_image_original = player.image.copy()

        def prep_score(self, settings, stats):
            """Render score image"""

            score_str = str(stats.score)
            self.score_image = self.font.render(score_str, True, self.color, settings.bg_color)

            self.score_rect.right = self.screen_rect.right - settings.score_offset
            self.score_rect.top = settings.score_offset

        def display_score(self, stats):
            """Display score to screen"""

            self.screen.blit(self.score_image, self.score_rect)

        def update_high_score(self, stats):
            """Updates high score"""

            if stats.score > self.high_score:
                self.high_score = stats.score

        def prep_high_score(self, settings, stats):
            """Render high score image"""

            high_score_str = str(self.high_score)
            self.high_score_image = self.font.render(high_score_str, True, self.color, settings.bg_color)

            self.high_score_rect.centerx = self.screen_rect.centerx
            self.high_score_rect.top = self.screen_rect.top + settings.score_offset

        def display_high_score(self, stats, settings):
            """Display high score to screen"""
            self.prep_high_score(settings, stats)
            self.screen.blit(self.high_score_image, self.high_score_rect)

        def update_lives(self, player):
            """Update number of lives displayed"""

            self.lives = player.lives


        def display_lives(self, settings, player):
            """Displaying all lives"""

            for i in range(0, player.lives):
                image = pygame.transform.rotate(self.lives_image_original.copy(), 90)
                rect = image.get_rect()
                rect.left = 1.5*settings.score_offset * (i+1)
                rect.top = settings.score_offset
                self.screen.blit(image, rect)
