'''
Menu example
'''

import sys
import pygame


pygame.init()

screen_mode = 'title'   # Modes: title, menu
FPS = 60

clock = pygame.time.Clock()
screen = pygame.display.set_mode([1200, 800])

# Title text
# font = pygame.font.SysFont('impact', 32)
# text_surface = font.render('Hello World!', True, [0,0,0], [0,255,0])

while True:
    screen.fill([0, 0, 5])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the screen
    pygame.display.update()
    clock.tick(FPS)
