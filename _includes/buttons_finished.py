'''
Buttons example
'''

import sys
import pygame

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# colors
RED = [255, 0, 0]
BLUE = [0, 0, 255]
DARK_RED = [200, 10, 10]
BLACK = [0, 0, 0]
GREY = [230, 230, 230]

# initialize pygame
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # Setup the game screen surface
clock = pygame.time.Clock()                                     # make a clock to manage FPS

font = pygame.font.SysFont('impact', 32) # Here's the font we'll use to render text

# Rect button
rect_button = pygame.Rect([10, 10], [100, 30])
rect_button_color = RED
rect_clicks = 0 # click tracker

# Image button
button_img = pygame.image.load('media/red-button.png') # Make an image surface
button_img_rect = button_img.get_rect()          # Get a bounding+drawing rectangle for the surface
                                                 # (this is what we'll use to detect collisions w/mouse)
button_img_rect.x = 10    # Position the img rectangle
button_img_rect.y = 100
button_img_clicks = 0 # click tracker

# Our game loop
while True:
    screen.fill(GREY)

    # CHALLENGE: if mouse if hovering over the button, make the color darker/outline it
    # We'll need to know the mouse position
    mouse_pos = pygame.mouse.get_pos()
    hover = False
    if rect_button.collidepoint(mouse_pos):
        # Mouse is over button
        print("Over RECT button!")
        rect_button_color = DARK_RED
        hover = True
    else:
        # Mouse not on button
        rect_button_color = RED

    ############################################################################
    # Draw the rectangle button
    pygame.draw.rect(screen, rect_button_color, rect_button)
    rect_clicks_surf = font.render(str(rect_clicks), True, BLACK)
    screen.blit(rect_clicks_surf, [rect_button.topright[0]+10, rect_button.topright[1]-5])
    # if we're hovering over the rectangle button,
    if hover:
        pygame.draw.rect(screen, BLACK, rect_button, 4)
    ############################################################################

    ############################################################################
    # Draw the image button
    screen.blit(button_img, button_img_rect)
    img_button_clicks_surf = font.render(str(button_img_clicks), True, BLACK)
    screen.blit(img_button_clicks_surf, [button_img_rect.topright[0]+10, button_img_rect.topright[1]-5])
    ############################################################################

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # when the mouse is clicked, did the player press any buttons?
            mouse_pos = pygame.mouse.get_pos()
            if rect_button.collidepoint(mouse_pos):
                # rectangle button was clicked
                print("RECTANGLE BUTTON CLICK")
                rect_clicks += 1
            if button_img_rect.collidepoint(mouse_pos):
                print("IMG BUTTON CLICK")
                button_img_clicks += 1

    pygame.display.update()
    clock.tick(FPS)