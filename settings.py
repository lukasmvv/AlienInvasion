import pygame.font


class Settings():
    """This class contains all the required settings for Alien Invasion"""

    def __init__(self):
        """Initialising settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.window_caption = "Alien Invasion!"

        # Ship settings
        self.ship_scale = 20
        self.ship_speed_increment = 1
        self.ship_max_speed = 2
        self.ship_image_path = "ship.png"
        self.ship_start_x = 0.3
        self.ship_rotate = -90
        self.ship_lives = 3
        self.ship_crash_sound_path = "ship_crash_sound.wav"
        self.ship_die_sound_path = "ship_die_sound.wav"

        # Bullets settings
        self.bullet_scale = 1
        self.bullet_speed_increment = 2
        self.bullet_max_speed = 4
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (60, 60, 60)
        self.bullet_fire_sound_path = "bullet_fire_sound.wav"

        # Alien settings
        self.alien_path = "alien.png"
        self.alien_speed_increment = 0.5
        self.alien_max_speed = 2
        self.alien_rotate = 0
        self.alien_scale = 15
        self.alien_tilt_max_angle = 30
        self.alien_tilt_increment = 1
        self.alien_tilt_frequency = 10
        self.alien_die_sound_path = "alien_die_sound.wav"
        self.alien_get_past_sound_path = "alien_get_past_sound.wav"

        # Game settings
        self.game_active = False
        self.player_hit_score = 0
        self.alien_gets_past_score = 20
        self.alien_hit_score = 100
        self.game_music_path = "game_music.mp3"
        self.background_image_path = "space_background.jpg"

        # Button settings
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)

        # Scoreboard settings
        self.scoreboard_text_color = (30, 30, 30)
        self.scoreboard_font = pygame.font.SysFont(None, 48)
        self.score_offset = 50