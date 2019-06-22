'''
Menu example
'''

import sys
import random
import pygame

pygame.init()

screen_mode = 'title'   # Modes: title, menu
FPS = 60
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BTN_PADDING = 10
BTN_MARGIN = 10

clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
menu_font = pygame.font.SysFont('impact', 32)

WHITE = [255, 255, 255]
GREY = [175, 175, 175]
BLACK = [0, 0, 5]
YELLOW = [255, 229, 153]
DARKER_YELLOW = [255, 217, 102]

menu_btn_color = YELLOW
menu_btn_hover_color = DARKER_YELLOW



################################################################################
# Title screen components
################################################################################
title_screen_bg_color = BLACK
# Title text
title_font = pygame.font.SysFont('impact', 128)
title_surface = title_font.render('THE MENU GAME', True, WHITE)
title_rect = title_surface.get_rect()
title_rect.x = (SCREEN_WIDTH / 2) - (title_rect.width / 2) # Put rect in middle of screen (perfectly in middle x)
title_rect.y = (SCREEN_HEIGHT / 2) - (title_rect.height)   # Put rect in middle of the screen (sitting on top of horizontal midline)

# Open menu button
menu_btn_txt_surface = menu_font.render('open menu', True, BLACK)

# setup menu button background
menu_btn_bg_rect = menu_btn_txt_surface.get_rect()
menu_btn_bg_rect.width += 2 * BTN_MARGIN  # Add some margins to the button
menu_btn_bg_rect.height += 2 * BTN_MARGIN # Add margin to the button
menu_btn_bg_rect.x = title_rect.midbottom[0] - (menu_btn_bg_rect.width / 2)
menu_btn_bg_rect.y = title_rect.midbottom[1] + BTN_PADDING

# setup text rectangle (used to determine where we'll draw text)
menu_btn_txt_rect = menu_btn_txt_surface.get_rect()
menu_btn_txt_rect.x = title_rect.midbottom[0] - (menu_btn_txt_rect.width / 2)
menu_btn_txt_rect.y = title_rect.midbottom[1] + BTN_PADDING + BTN_MARGIN

################################################################################
# Menu screen components
################################################################################
menu_screen_bg_color = GREY

menu_screen_buttons = ['resume', 'random', 'quit']
cur_menu_btn_id = 0
btn_color = YELLOW

# Render resume btn text onto surface
resume_btn_txt_surface = menu_font.render('Resume', True, BLACK)
# Setup resume button background
resume_btn_bg_rect = resume_btn_txt_surface.get_rect()
resume_btn_bg_rect.width += 2 * BTN_MARGIN
resume_btn_bg_rect.height += 2 * BTN_MARGIN
resume_btn_bg_rect.x = (SCREEN_WIDTH / 2) - (0.5 * resume_btn_bg_rect.width)
resume_btn_bg_rect.y = 50
# Setup the resume button text
resume_btn_txt_rect = resume_btn_txt_surface.get_rect()
resume_btn_txt_rect.x = resume_btn_bg_rect.x + BTN_MARGIN
resume_btn_txt_rect.y = resume_btn_bg_rect.y + BTN_MARGIN

# Render random btn text onto surface
random_btn_txt_surface = menu_font.render('???', True, BLACK)
# Setup random button background
random_btn_bg_rect = random_btn_txt_surface.get_rect()
random_btn_bg_rect.width += 2 * BTN_MARGIN
random_btn_bg_rect.height += 2 * BTN_MARGIN
random_btn_bg_rect.x = (SCREEN_WIDTH / 2) - (0.5 * random_btn_bg_rect.width)
random_btn_bg_rect.y = resume_btn_bg_rect.y + (resume_btn_bg_rect.height + BTN_PADDING)
# Setup the random button text
random_btn_txt_rect = random_btn_txt_surface.get_rect()
random_btn_txt_rect.x = random_btn_bg_rect.x + BTN_MARGIN
random_btn_txt_rect.y = random_btn_bg_rect.y + BTN_MARGIN

# Render quit btn text onto surface
quit_btn_txt_surface = menu_font.render('Quit', True, BLACK)
# Setup quit button background
quit_btn_bg_rect = quit_btn_txt_surface.get_rect()
quit_btn_bg_rect.width += 2 * BTN_MARGIN
quit_btn_bg_rect.height += 2 * BTN_MARGIN
quit_btn_bg_rect.x = (SCREEN_WIDTH / 2) - (0.5 * quit_btn_bg_rect.width)
quit_btn_bg_rect.y = random_btn_bg_rect.y + (resume_btn_bg_rect.height + BTN_PADDING)
# Setup the quit button text
quit_btn_txt_rect = quit_btn_txt_surface.get_rect()
quit_btn_txt_rect.x = quit_btn_bg_rect.x + BTN_MARGIN
quit_btn_txt_rect.y = quit_btn_bg_rect.y + BTN_MARGIN


while True:
    # We need to show different things depending on whether or not we're in 'title'
    # or 'menu' mode
    if screen_mode == 'title':
        # ==== TITLE SCREEN MODE ====
        screen.fill(title_screen_bg_color)
        # Draw the title screen
        # Render the title text in the middle of the screen
        screen.blit(title_surface, title_rect)
        # Draw the menu button, first: the text
        pygame.draw.rect(screen, menu_btn_color, menu_btn_bg_rect)
        screen.blit(menu_btn_txt_surface, menu_btn_txt_rect)
    elif screen_mode == 'menu':
        # === MENU SCREEN MODE ===
        screen.fill(menu_screen_bg_color)
        # Draw button rectangles!
        # - If button is active, color background with hover color and an outline
        # - otherwise, draw with normal color and no outline
        if menu_screen_buttons[cur_menu_btn_id] == 'resume':
            pygame.draw.rect(screen, menu_btn_hover_color, resume_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, resume_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, resume_btn_bg_rect)

        if menu_screen_buttons[cur_menu_btn_id] == 'random':
            pygame.draw.rect(screen, menu_btn_hover_color, random_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, random_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, random_btn_bg_rect)

        if menu_screen_buttons[cur_menu_btn_id] == 'quit':
            pygame.draw.rect(screen, menu_btn_hover_color, quit_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, quit_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, quit_btn_bg_rect)

        # Layer button text over button backgrounds
        screen.blit(resume_btn_txt_surface, resume_btn_txt_rect)
        screen.blit(random_btn_txt_surface, random_btn_txt_rect)
        screen.blit(quit_btn_txt_surface, quit_btn_txt_rect)
    else:
        # ==== ???? MODE ====
        print("AAAH UNRECOGNIZED SCREEN MODE! Exiting")
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # TITLE MODE EVENTS
        if screen_mode == 'title' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if menu_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'menu'
                cur_menu_btn_id = 0
        # MENU MODE EVENTS
        if screen_mode == 'menu' and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                cur_menu_btn_id = (cur_menu_btn_id + 1) % len(menu_screen_buttons)
            if event.key == pygame.K_UP:
                cur_menu_btn_id = (cur_menu_btn_id - 1) % len(menu_screen_buttons)
            if event.key == pygame.K_RETURN:
                if menu_screen_buttons[cur_menu_btn_id] == 'resume':
                    screen_mode = 'title'
                elif menu_screen_buttons[cur_menu_btn_id] == 'random':
                    menu_screen_bg_color = [random.randint(0, 255),
                                            random.randint(0, 255),
                                            random.randint(0, 255)]
                elif menu_screen_buttons[cur_menu_btn_id] == 'quit':
                    pygame.quit()
                    sys.exit()
