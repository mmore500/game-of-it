'''
Buttons example
'''

import sys
import pygame

FPS = 60

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([1200, 800])

font = pygame.font.SysFont('impact', 32)

RED = [255, 0, 0]
BLUE = [0, 0, 255]
DARK_RED = [200, 10, 10]
BLACK = [0, 0, 0]

# Rect button
rect_button = pygame.Rect([10, 10], [100, 30])
rect_button_color = RED
rect_clicks = 0

# Image button
button_img = pygame.image.load('red-button.png')
button_img_rect = button_img.get_rect()
button_img_rect.x = 10
button_img_rect.y = 100
button_img_clicks = 0

while True:
    screen.fill([200,200,200])

    # If mouse is hoving over button, color differently


    mouse_pos = pygame.mouse.get_pos()

    ############################################################################
    # Draw the rectangle button
    hover = False
    if rect_button.collidepoint(mouse_pos):
        # Mouse is over button
        print("Over RECT button!")
        rect_button_color = DARK_RED
        hover = True
    else:
        # Mouse not on button
        rect_button_color = RED

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
            mouse_pos = pygame.mouse.get_pos()
            if rect_button.collidepoint(mouse_pos):
                rect_clicks += 1
            if button_img_rect.collidepoint(mouse_pos):
                button_img_clicks += 1

    pygame.display.update()
    clock.tick(FPS)