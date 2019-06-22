'''
Code copied and adapted from https://inventwithpython.com/pygame/chapter2.html
'''

import sys
import random
import pygame

pygame.init()

FPS = 30 # Frames per second
fps_clock = pygame.time.Clock() # Helps us make sure our programs run at a certain maximum FPS
                                # It'll put small pauses each iteration through our game loop

# Setup the window
width = 400
height = 300
display_surface = pygame.display.set_mode([width, height], 0, 32)
pygame.display.set_caption('Catmation!')

cat_img = pygame.image.load('cat.png')
cat_x = 10
cat_y = 10

direction = 'left'
while True: # Enter the game loop
    display_surface.fill([255, 255, 255])

    # Position the cat randomly
    # cat_x = random.randint(0, width)
    # cat_y = random.randint(0, height)

    # CHALLENGE: have the cat infinitely pace back and forth (move to the right
    #   until it reaches an edge, then move left, etc)

    # -- Challenge code --
    # if direction == 'right':
    #     # Move to the right
    #     cat_x += 5
    #     if cat_x >= 280: # Need to change directions
    #         direction = 'left'
    #         # cat_img = pygame.transform.flip(cat_img, True, False)


    # elif direction == 'left':
    #     # Move to the left
    #     cat_x -= 5
    #     if cat_x <= 20: # Need to change directions
    #         direction = 'right'
            # cat_img = pygame.transform.flip(cat_img, True, False)

    # Question: why does the back and forth look the way it does?
    # Follow-up: can you make the cat go in a square loop?
    #            - What about a circular loop?
    # Follow-up: can you make the cat face the direction it's moving?
    #            - Look into pygame.transform

    # Update cat
    display_surface.blit(cat_img, [cat_x, cat_y]) # Blit draws something on the surface


    # Setup the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the screen
    pygame.display.update()
    fps_clock.tick(FPS)     # Tick the clock!
