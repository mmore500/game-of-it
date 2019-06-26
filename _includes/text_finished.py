'''
Rending text

Code copied and adapted from https://inventwithpython.com/pygame/chapter2.html
'''

import sys
import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

screen_width = 400
screen_height = 300
display_bg_color = [255,255,255]

display_surface = pygame.display.set_mode([screen_width, screen_height])
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
hello_color = [0,0,0]
hello_bg = [0,255,0]
hello_surface = font.render('Hello World!', True, hello_color, hello_bg)

# Where do we want to draw the text?
hello_x = screen_width / 2
hello_y = screen_height / 2

# CHALLENGE: add some more text to the screen, try rendering a few different fonts
#            at once
goodbye_color = [255,255,255]
goodbye_bg = [0,0,0]
goodbye_surface = font.render('Goodbye forever!', True, goodbye_color, goodbye_bg)
goodbye_x = 0
goodbye_y = 0

# CHALLENGE: just like the cat animation, can you make some text move around?
moving_text_color = [0,0,0]
moving_text_surface = font.render('MOVING', True, moving_text_color)
moving_text_bounding_rect = moving_text_surface.get_rect()
moving_text_bounding_rect.x = screen_width - moving_text_surface.get_rect().width
moving_text_bounding_rect.y = 0
moving_text_dir = 'southwest'

# rot_degrees = 1
while True:
    # fill the background
    display_surface.fill(display_bg_color)

    # blit the text onto the screen
    # - The top left corner of the text should be at hello_x, hello_y
    display_surface.blit(hello_surface, [hello_x, hello_y])

    # blit goodbye to the screen
    display_surface.blit(goodbye_surface, [goodbye_x, goodbye_y])

    # Animate the moving text
    if moving_text_dir == 'southwest':
        moving_text_bounding_rect.x -= 1 # Move text to the left by 1
        moving_text_bounding_rect.y += 1 # Move text down by 1
        if (moving_text_bounding_rect.bottomleft[1] >= screen_height) or (moving_text_bounding_rect.x <= 0):
            moving_text_dir = 'northeast'
    elif moving_text_dir == 'northeast':
        moving_text_bounding_rect.x += 1 # Move text to the right by 1
        moving_text_bounding_rect.y -= 1 # Move text up by 1
        if (moving_text_bounding_rect.topright[1] <= 0) or (moving_text_bounding_rect.x >= screen_width):
            moving_text_dir = 'southwest'

    # blit the moving text
    display_surface.blit(moving_text_surface, moving_text_bounding_rect)

    # Events!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()
    clock.tick(FPS)