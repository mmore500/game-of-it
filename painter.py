'''
This game acts like a painter tool. The first line changes color. The second line changes the background.
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
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Collider Demo")

# Make a clock to manage frames per second
clock = pygame.time.Clock()

mouse_rect = pygame.Rect([0,0], [30, 30])
wall_rect = pygame.Rect([400, 400], [30, 600])
sec_wall_rect = pygame.Rect([700,200], [30, 900])
# Game loop
mouse_rect_color = [0,0,0]

already_changed_color = False
screen.fill(LIGHT_GREY)
while True:
    # Set the background color
    
    
    mouse_position = pygame.mouse.get_pos()
    mouse_rect.centerx = mouse_position[0]
    mouse_rect.centery = mouse_position[1]
    
    if mouse_rect.colliderect(wall_rect):
        R = random.randint(0,255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        
        mouse_rect_color=[R, G, B]
    if mouse_rect.colliderect(sec_wall_rect):
        if not already_changed_color:
            R = random.randint(0,255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
            screen.fill([R, G, B])
            already_changed_color = True
    else:
        already_changed_color = False

    pygame.draw.rect(screen, [0,0,0], wall_rect)
    pygame.draw.rect(screen, mouse_rect_color, mouse_rect)
    pygame.draw.rect(screen, [0,0,0], sec_wall_rect)

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
