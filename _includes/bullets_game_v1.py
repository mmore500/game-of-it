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
character = {"rect":pygame.Rect([char_start_x, char_start_y], [char_width, char_height]),
             "dir": "right",
             "x_vel": 0,
             "y_vel": 0,
             "color": BLUE}

bullets = [] # Here's where we'll track all of the bullets on the screen
bullet_speed = 10 # How fast should bullets move?
bullet_width = 7.5
bullet_height = 5

enemy_width = 50
enemy_height = 50
enemies = [{"rect": pygame.Rect([900,100],[enemy_width,enemy_height]), "dir": "left"},
           {"rect": pygame.Rect([900,700],[enemy_width,enemy_height]), "dir": "left"}]


# Game loop
while True:
    screen.fill(LIGHT_GREY)

    # Determine character movement
    # Is the player pressing a key?
    # - Is player moving vertically?
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        print("up arrow")
        character["y_vel"] = -1*char_speed
    elif pressed_keys[pygame.K_DOWN]:
        print("down arrow")
        character["y_vel"] = char_speed
    else:
        character["y_vel"] = 0
    # - Is player moving horizontally?
    if pressed_keys[pygame.K_RIGHT]:
        print("down arrow")
        character["x_vel"] = char_speed
    elif pressed_keys[pygame.K_LEFT]:
        print("down arrow")
        character["x_vel"] = -1*char_speed
    else:
        character["x_vel"] = 0

    # Draw the character!
    character["rect"].left += character["x_vel"]
    character["rect"].top += character["y_vel"]
    pygame.draw.rect(screen, BLUE, character["rect"])
    # - indicate where character is facing
    if character["dir"] == "up":
        pos = character["rect"].midtop
        pygame.draw.rect(screen, BLACK, pygame.Rect([pos[0], pos[1]-5], [5, 5]))
    elif character["dir"] == "down":
        pos = character["rect"].midbottom
        pygame.draw.rect(screen, BLACK, pygame.Rect([pos[0], pos[1]], [5, 5]))
    elif character["dir"] == "right":
        pos = character["rect"].midright
        pygame.draw.rect(screen, BLACK, pygame.Rect([pos[0], pos[1]], [5, 5]))
    elif character["dir"] == "left":
        pos = character["rect"].midleft
        pygame.draw.rect(screen, BLACK, pygame.Rect([pos[0]-5, pos[1]], [5, 5]))

    # Draw the enemies!
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy["rect"])

    # Draw the bullets!
    # Challenge: Every time you click, fire bullets from your mouse
    # Challenge: Have bullets that collide with enemies remove that enemy from the screen
    # Challenge: clean up off-screen bullets
    # Challange: spawn new enemies
    on_screen_bullets = []
    for bullet in bullets:
        # What direction is the bullet going?
        if bullet["dir"] == "up":
            bullet["rect"].top -= bullet_speed
        elif bullet["dir"] == "right":
            bullet["rect"].left += bullet_speed
        elif bullet["dir"] == "down":
            bullet["rect"].top += bullet_speed
        elif bullet["dir"] == "left":
            bullet["rect"].left -= bullet_speed

        # bullet["rect"].left += bullet_speed
        pygame.draw.rect(screen, BLACK, bullet["rect"])

        alive_enemies = []
        for enemy in enemies:
            if bullet["rect"].colliderect(enemy["rect"]):
                print(random.choice(["AAAAHHHH","GRUNT", "UUUGGG", "SPLAT", "POP"]))
                continue
            alive_enemies.append(enemy)

        enemies = alive_enemies

        if bullet["rect"].left <= screen_width:
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
                pos = [0, 0]
                if character["dir"] == "up":
                    pos = character["rect"].midtop
                    h = bullet_width
                    w = bullet_height
                elif character["dir"] == "down":
                    pos = character["rect"].midbottom
                    h = bullet_width
                    w = bullet_height
                elif character["dir"] == "right":
                    pos = character["rect"].midright
                    h = bullet_height
                    w = bullet_width
                elif character["dir"] == "left":
                    pos = character["rect"].midleft
                    h = bullet_height
                    w = bullet_width
                bullet = {"rect": pygame.Rect(pos[0], pos[1], w, h), "dir": character["dir"]}
                bullets.append(bullet)
            if event.key == pygame.K_w:
                character["dir"] = "up"
            if event.key == pygame.K_d:
                character["dir"] = "right"
            if event.key == pygame.K_s:
                character["dir"] = "down"
            if event.key == pygame.K_a:
                character["dir"] = "left"


    pygame.display.update()
    clock.tick(FPS)

# Challenges:
# - Add enemy spawns
# - Add enemy movement
# - Add enemy shooting
