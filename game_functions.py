import sys
import pygame
from bullet import Bullet
from alien import Alien
import pygame.mixer


def check_events(player, screen, settings, bullets, new_game, stats, aliens, sb):
    """Function to check input events from player"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, player, screen, settings, bullets, stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            check_key_up(event, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, new_game, settings, stats, aliens, bullets, player, sb)


def check_play_button(mouse_x, mouse_y, new_game, settings, stats, aliens, bullets, player, sb):
    """Checks if the play button has been clicked"""

    if new_game.rect.collidepoint(mouse_x, mouse_y) and not settings.game_active:

        # Restart game
        restart_game(settings, stats, aliens, bullets, player, sb)


def restart_game(settings, stats, aliens, bullets, player, sb):
    """Restarts the game"""

    settings.game_active = True
    stats.reset_stats()
    sb.prep_score(settings, stats)

    # Hide cursor
    pygame.mouse.set_visible(False)

    # Empty aliens and bullets
    aliens.empty()
    bullets.empty()

    # Reset ship position
    player.lives = settings.ship_lives
    player.rect.centerx = int(player.ship_starting_scale_x * player.screen_rect.right)
    player.rect.centery = int(player.screen_rect.centery)


def check_key_down(event, player, screen, settings, bullets, stats, aliens, sb):
    """Responds to key presses"""

    # Ship movement
    if settings.game_active:
        if event.key == pygame.K_RIGHT:
            player.moving_right = True
        if event.key == pygame.K_LEFT:
            player.moving_left = True
        if event.key == pygame.K_UP:
            player.moving_up = True
        if event.key == pygame.K_DOWN:
            player.moving_down = True

        # Ship firing
        if event.key == pygame.K_SPACE:
            fire_bullet(screen, settings, player, bullets)

    # Quit game
    if event.key == pygame.K_q:
        sys.exit()

    # Restart game
    if event.key == pygame.K_r:
        restart_game(settings, stats, aliens, bullets, player, sb)


def check_key_up(event, player):
    """Responds to key releases"""

    # Ship movement
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    if event.key == pygame.K_LEFT:
        player.moving_left = False
    if event.key == pygame.K_UP:
        player.moving_up = False
    if event.key == pygame.K_DOWN:
        player.moving_down = False


def update_screen(screen, settings, player, bullets, aliens, new_game, sb, stats, bg_image):
    """Function to update game screen"""

    # Redraw the screen
    add_background_image(screen, settings, bg_image)

    # Redraw ship
    player.blitme()

    # Drawing all bullets
    for bullet in bullets:
        bullet.draw_bullet()

    # Draw all the aliens
    for alien in aliens:
        alien.blitme()

    # Draw button
    if not settings.game_active:
        new_game.draw_button()

    # Display score
    sb.display_score(stats)

    # Display high score
    sb.update_high_score(stats)
    sb.display_high_score(stats, settings)

    # Display number of lives
    sb.display_lives(settings, player)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def add_background_image(screen, settings, image):
    """Function to set background image"""

    screen.blit(image, (0, 0))

def fire_bullet(screen, settings, player, bullets):
    """Function that fires bullet"""

    new_bullet = Bullet(screen, settings, player)
    bullets.add(new_bullet)

    # Play sound
    play_sound(settings.bullet_fire_sound_path)


def update_bullets(bullets, screen, aliens, stats, settings, sb):
    """This function updates the bullets by checking position and dremoving from group"""

    # Update bullets positions
    for bullet in bullets:
        bullet.update_position()

    # Checking if bullet is out of screen
    for bullet in bullets.copy():  # never remove items from within a for loop, so use a copy
        if bullet.rect.left > screen.get_rect().right:
            bullets.remove(bullet)
    # print(len(bullets))

    # Checking for bullet collisions with alien ships
    # groupcollide loops through each group to check for collisions
    # Whenever the rects of a bullet and alien overlap, we get a key-value pair in a dictionary
    # The true arguments tells python to delete the collided objects
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # Play sound
        play_sound(settings.alien_die_sound_path)

        stats.score += settings.alien_hit_score
        sb.prep_score(settings, stats)

    #if collisions:
     #   print(collisions)
      #  msg = input("Pause")


def check_alien_counter(counter, aliens, screen, settings):
    """This function determines if a new alien should be created"""

    if counter > 1000:
        aliens.add(Alien(screen, settings))
        counter = 0

    return counter


def update_aliens(aliens, player, settings, stats, screen, sb):
    """This function updates aliens positions and checks for collisions with players"""

    # Updating alien position
    for alien in aliens:
        alien.update_position()

    # Checking for alien reaching left screen
    for alien in aliens.copy():  # never remove items from within a for loop, so use a copy
        if alien.rect.right < screen.get_rect().left:
            # Play sound
            play_sound(settings.alien_get_past_sound_path)

            # Remove alien from group and decrease score
            aliens.remove(alien)
            stats.score -= settings.alien_gets_past_score
            sb.prep_score(settings, stats)
    # print(len(aliens))

    # Checking for collisions with player
    # spritecollideany takes 2 arguments: a sprite and a group (player and aliens)
    # spritecollide checks for a sprite colliding with a group and deletes item in group if dokill=True

    # player is has been hit
    if pygame.sprite.spritecollide(player, aliens, True) and not player.hit:
        player.hit = not player.hit
        stats.score -= settings.player_hit_score
        aliens.remove()
        ship_hit(player, settings, sb, stats)
    # player ship is still being hit
    elif pygame.sprite.spritecollide(player, aliens, False) and player.hit:
        pass
    # player ship was hit but currently not hit
    elif not pygame.sprite.spritecollide(player, aliens, False) and player.hit:
        player.hit = not player.hit


def ship_hit(player, settings, sb, stats):
    """Handles code when player ship is hit"""

    # Decrease lives
    player.lives -= 1
    sb.prep_score(settings, stats)
    sb.update_lives(player)
    if player.lives == 0:

        # Play sound
        play_sound(settings.ship_die_sound_path)

        # Game settings
        settings.game_active = not settings.game_active
        pygame.mouse.set_visible(True)

    else:
        # Play sound
        play_sound(settings.ship_crash_sound_path)


def play_sound(path):
    """Play a sound on a channel"""

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(path))