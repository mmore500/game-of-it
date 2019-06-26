'''
Rendering text

Code copied and adapted from https://inventwithpython.com/pygame/chapter2.html
'''

import sys
import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

width = 400
height = 300
display_bg_color = [255,255,255]
display_surface = pygame.display.set_mode([width, height])
pygame.display.set_caption('This window will have some text in it. Woo?')

# Font documentation: https://www.pygame.org/docs/ref/font.html

# use the pygame.font.get_fonts() function to get a list of available fonts on your
# system
print('Available fonts:', pygame.font.get_fonts())

# To render text with pygame, first we need to create a font
# - when we create a font, we tell it which font-style to use and what font size
#   we want.
# - CHALLENGE: try changing the font size and the font type (use get_fonts() to
#              figure out what is possible)
font = pygame.font.SysFont('impact', 32)
# Next, we can render the font onto a surface (which we'll eventually draw on the
# display_display surface)
# - To render text, we need to specify: (1) the string we want to write, (2) use
#   anti-aliasing? (smoothing technique), (3) what color we want the text to be?,
#   and (4) what background color we want? (if blank, no background color)
text_color = [0,0,0]
text_bg = [0,255,0]
text_surface = font.render('Hello World!', True, text_color, text_bg)
# Where do we want to draw the text?
text_x = width / 2
text_y = height / 2

# CHALLENGE: add some more text to the screen, try rendering a few different fonts
#            at once

while True:
    # fill the background
    display_surface.fill(display_bg_color)

    # CHALLENGE: WORD ANIMATION => Use pygame.transform to animate the text

    # blit the text onto the screen
    display_surface.blit(text_surface, [text_x, text_y])

    # Events!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()
    clock.tick(FPS)