'''
Bullet shooter
'''
import sys
import random
import pygame

pygame.init() # Initialize pygame

# Some constant values
screen_width = 1200
screen_height = 800
FPS = 60                # Frames per second

# colors
RED = [255, 0, 0]
LIGHT_GREY = [230, 230, 230]
BLACK = [0, 0, 0]

# Setup the screen surface
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Bullet Shooter")

clock = pygame.time.Clock() # Get a clock to manage FPS

# Projectiles!
bullets = []            # Here's where we'll track all of the bullets on the screen
bullet_velocity_x = 10  # How fast should bullets move?
bullet_width = 7.5
bullet_height = 5

# Targets!
enemy_width = 50
enemy_height = 50
# We'll start with two, statically placed targets
enemies = [pygame.Rect([900,100],[enemy_width,enemy_height]), pygame.Rect([900,700],[enemy_width,enemy_height])]

# Game loop
while True:
    screen.fill(LIGHT_GREY)

    # Draw the enemies!
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Challenge: (1) Every time you click, fire bullets from your mouse
    # Challenge: (2) clean up off-screen bullets
    # Challenge: (3) Have bullets that collide with enemies remove that enemy from the screen
    # Challange: (4) spawn new enemies randomly
    # Challenge: (5) spawn enemy when you press the spacebar

    # Draw the projectiles
    # - We don't need to track projectiles that go offscreen anymore (in fact, we
    #   really shouldn't track those), so we'll keep track of what projectiles are
    #   still on screen with on_screen_bullets
    on_screen_bullets = []
    for bullet in bullets:
        bullet.left += bullet_velocity_x        # Apply movement
        pygame.draw.rect(screen, BLACK, bullet) # Draw the bullet

        # Does this bullet collide with any enemies?
        alive_enemies = []                      # We'll use this to track which
                                                # enemies are still alive after handling this bullet
        for enemy in enemies:
            if bullet.colliderect(enemy):
                # If bullet collides, make some noise, and don't add to alive enemies list
                print(random.choice(["AAAAHHHH","GRUNT", "UUUGGG", "SPLAT", "POP"]))
                continue
            alive_enemies.append(enemy) # Enemy escaped the projectile
        enemies = alive_enemies # Update enemies list

        # Is this projectile still on screen?
        if bullet.left <= screen_width:
            on_screen_bullets.append(bullet)

    # Update list of projectiles with only those that are still on screen
    bullets = on_screen_bullets

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Fire bullet when player presses mouse button
            pos = pygame.mouse.get_pos()
            bullet = pygame.Rect(pos[0], pos[1], bullet_width, bullet_height)
            bullets.append(bullet)
            print(len(bullets))

    pygame.display.update() # update the screen
    clock.tick(FPS)
