'''
Collision detection
'''

import sys
import random
import pygame

# Initialize pygame
pygame.init()

# Some constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

LIGHT_GREY = [230, 230, 230]

# Create the display surface
display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Collider Demo")

# Make a clock to manage frames per second
clock = pygame.time.Clock()

# Make a rectangle that will follow the mouse around
my_rect = pygame.Rect(100, 200, 30, 150)
# Make a wall (rectangle) that we'll have the mouse-following rectangle collide with
wall = pygame.Rect(400, 400, 30, 600)

# Game loop
while True:
    # Set the background color
    display.fill(LIGHT_GREY)

    # my_rect is going to follow the mouse around => we need to get the mouse's x,y position
    pos = pygame.mouse.get_pos()
    my_rect.centerx = pos[0]
    my_rect.centery = pos[1]

    # To start, mouse rectangle will be black
    color = [0, 0, 0]
    if my_rect.colliderect(wall): # <==== Here's where the collision magic happens
        # If there's a collision, randomize the mouse-rectangle's color
        print("collide")
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    # Draw both the mouse rectangle and th e wall
    pygame.draw.rect(display, [0,0,0], wall)
    pygame.draw.rect(display, color, my_rect)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display, tick clock
    pygame.display.update()
    clock.tick(FPS)

# CHALLENGE: Add a few more obstacles to the scene and test for collisions between
#            the mouse and those obstacles
#             - bonus: trigger different reactions depending on which obstacle you
#                       hit with the mouse-following rectangle
