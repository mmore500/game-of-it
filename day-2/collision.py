'''
Collision detection
'''

import sys
import random
import pygame

pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("Collider Demo")

LIGHT_GREY = [230, 230, 230]

# my_rect = pygame.Rect(100, 200, 30, 150)
# wall = pygame.Rect(400, 400, 30, 600)

# color = [0, 0, 0]

# Game loop
while True:
    # Set the background color
    display.fill(LIGHT_GREY)

    # my_rect is going to follow the mouse around => we need to get the mouse's x,y position
    # pos = pygame.mouse.get_pos()
    # my_rect.centerx = pos[0]
    # my_rect.centery = pos[1]

    # if my_rect.colliderect(wall):
    #     # print("collide")
    #     color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    # pygame.draw.rect(display, [0,0,0], wall)
    # pygame.draw.rect(display, color, my_rect)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update the display, tick clock
    pygame.display.update()
    clock.tick(60)