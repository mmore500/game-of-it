'''
Bullet shooter game
'''

import sys
import random
import pygame

pygame.init()

# let's try to avoid magic numbers for this
screen_width = 1200
screen_height = 800
FPS = 60

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Bullet Shooter")

clock = pygame.time.Clock()

RED = [255, 0, 0]
LIGHT_GREY = [230, 230, 230]
BLACK = [0, 0, 0]
BLUE = [0,0,230]

char_start_x = 0
char_start_y = 0
char_width = 50
char_height = 50
char_speed = 5      # How fast does character move?
cur_char_x_vel = 0  # What's the character's current x speed?
cur_char_y_vel = 0  # What's the character's current y speed?
character = pygame.Rect([char_start_x, char_start_y], [char_width, char_height])

bullets = [] # Here's where we'll track all of the bullets on the screen
bullet_velocity_x = 10 # How fast should bullets move?
bullet_width = 7.5
bullet_height = 5

enemy_width = 50
enemy_height = 50
enemies = [pygame.Rect([900,100],[enemy_width,enemy_height]), pygame.Rect([900,700],[enemy_width,enemy_height])]

# Game loop
while True:
    screen.fill(LIGHT_GREY)

    # Determine character movement
    # Is the player pressing a key?
    # - Is player moving vertically?
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        print("up arrow")
        cur_char_y_vel = -1*char_speed
    elif pressed_keys[pygame.K_DOWN]:
        print("down arrow")
        cur_char_y_vel = char_speed
    else:
        cur_char_y_vel = 0
    # - Is player moving horizontally?
    if pressed_keys[pygame.K_RIGHT]:
        print("down arrow")
        cur_char_x_vel = char_speed
    elif pressed_keys[pygame.K_LEFT]:
        print("down arrow")
        cur_char_x_vel = -1*char_speed
    else:
        cur_char_x_vel = 0

    # Draw the character!
    character.left += cur_char_x_vel
    character.top += cur_char_y_vel
    pygame.draw.rect(screen, BLUE, character)

    # Draw the enemies!
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Draw the bullets!
    # Challenge: Every time you click, fire bullets from your mouse
    # Challenge: Have bullets that collide with enemies remove that enemy from the screen
    # Challenge: clean up off-screen bullets
    # Challange: spawn new enemies
    on_screen_bullets = []
    for bullet in bullets:
        bullet.left += bullet_velocity_x
        pygame.draw.rect(screen, BLACK, bullet)

        alive_enemies = []
        for enemy in enemies:
            if bullet.colliderect(enemy):
                print(random.choice(["AAAAHHHH","GRUNT", "UUUGGG", "SPLAT", "POP"]))
                continue
            alive_enemies.append(enemy)

        enemies = alive_enemies

        if bullet.left <= screen_width:
            on_screen_bullets.append(bullet)
    bullets = on_screen_bullets

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Keydown event!
            if event.key == pygame.K_SPACE:
                # Fire a bullet
                print("pressed space")
                print(character.midright)
                pos = character.midright
                bullet = pygame.Rect(pos[0], pos[1], bullet_width, bullet_height)
                bullets.append(bullet)


    pygame.display.update()
    clock.tick(FPS)
