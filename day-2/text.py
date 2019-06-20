'''
Rending text

Code copied and adapted from https://inventwithpython.com/pygame/chapter2.html
'''

import sys
import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

width = 400
height = 300
display_surface = pygame.display.set_mode([width, height])
pygame.display.set_caption('This window will have some text in it. Woo?')

# Font documentation: https://www.pygame.org/docs/ref/font.html

print('Available fonts:', pygame.font.get_fonts())

font = pygame.font.SysFont('impact', 32)
text_surface = font.render('Hello World!', True, [0,0,0], [0,255,0])

text_x = width/2
text_y = height/2

# rot_degrees = 1
while True:
    # fill the background
    display_surface.fill([255,255,255])

    # Challenge: WORD ANIMATION => Use pygame.transform to animate the text
    # text_surface = font.render('Hello World!', True, [0,0,0], [0,255,0])
    # text_surface = pygame.transform.rotate(text_surface, rot_degrees)
    # rot_degrees += 1

    # blit the text onto the screen
    display_surface.blit(text_surface, [text_x, text_y])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()
    clock.tick(FPS)