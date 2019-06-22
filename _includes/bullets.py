'''
Bullet shooter
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

    # Draw the enemies!
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

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
        if event.type == pygame.MOUSEBUTTONUP:
            # Fire bullet
            pos = pygame.mouse.get_pos()
            bullet = pygame.Rect(pos[0], pos[1], bullet_width, bullet_height)
            bullets.append(bullet)
            print(len(bullets))

    # Challenge: play with mouse events

    pygame.display.update()
    clock.tick(FPS)
