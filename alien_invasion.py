import pygame
import pygame.mixer
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialize pygame, settings and screen object"""
    pygame.init()  # initialized background settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.window_caption)

    # Create game stats
    stats = GameStats(settings)

    # Make a player ship
    player = Ship(screen, settings)

    # Make a group for bullets to be stored in
    bullets = Group()  # acts like a specialized list

    # Make a group for aliens to be stored in
    aliens = Group()

    # Alien counter
    counter = 0

    # New game button
    new_game = Button(settings, screen, "New Game")

    # Making scoreboard
    sb = Scoreboard(stats, screen, settings, player)

    # Playing sound
    pygame.mixer.music.load(settings.game_music_path)
    pygame.mixer.music.play(-1)

    # Get background image and resize
    bg_image_org = pygame.image.load(settings.background_image_path).convert()
    bg_image = pygame.transform.smoothscale(bg_image_org.copy(), (settings.screen_width, settings.screen_height))

    # Start the main loop for the game
    while True:

        # Watch for keyboard events
        gf.check_events(player, screen, settings, bullets, new_game, stats, aliens, sb)

        if settings.game_active:
            # Update ship position
            player.update_position()

            # Checking if alien should be added
            counter = gf.check_alien_counter(counter, aliens, screen, settings)

            # Update aliens
            gf.update_aliens(aliens, player, settings, stats, screen, sb)

            # Update bullets
            gf.update_bullets(bullets, screen, aliens, stats, settings, sb)

            counter += 1
        else:


            #sleep(1)
            #print("Game ends")
            #break
            pass

        # Update screen
        gf.update_screen(screen, settings, player, bullets, aliens, new_game, sb, stats, bg_image)

run_game()