'''
2D Portal Game
'''
import time
import sys
import random
import pygame
import math

# Constants
FPS = 60
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 615
BTN_PADDING = 10    # How much padding are we going to put around a button?
BTN_MARGIN = 10     # How much space do we want around button text?

# Colors
GREEN = [10, 230, 20]
WHITE = [255, 255, 255]
GREY = [175, 175, 175]
BLACK = [0, 0, 5]
YELLOW = [255, 229, 153]
DARKER_YELLOW = [255, 217, 102]
ORANGE = [255, 165, 0]
ASCREEN = pygame.image.load("title.png")


pygame.init() # As always, initialize pygame

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
menu_font = pygame.font.SysFont('impact', 32)   # Here's our button font
print("Loaded the font!")
screen_mode = 'title'   # Modes: title, menu

menu_btn_color = WHITE
menu_btn_hover_color = GREY


################################################################################
# Title screen components
################################################################################
title_screen_bg = pygame.image.load("title.png")

##############################################################################
                # Level Menu
##############################################################################

Levels_screen_bg = pygame.image.load("Levels.png")

Levels_screen_buttons = ['Level One', 'Level Two', 'Level Three', 'back'] # Available buttons
cur_menu_btn_id = 0                                # What button are we currently on?
btn_color = YELLOW
# === Title text ===
title_font = pygame.font.SysFont('impact', 128)
title_surface = title_font.render('PORTAL', True, WHITE)
title_rect = title_surface.get_rect()
title_rect.x = 50
title_rect.y = 300
# === Open menu button ===
Levels_btn_txt_surface = menu_font.render('back', True, BLACK)
menu_btn_txt_surface = menu_font.render('Start', True, BLACK)
Levels_btn_bg_rect = Levels_btn_txt_surface.get_rect()
menu_btn_bg_rect = menu_btn_txt_surface.get_rect()
#size correctly
menu_btn_bg_rect.width += (2*BTN_MARGIN)
menu_btn_bg_rect.height += (2*BTN_MARGIN)
#position it
menu_btn_bg_rect.x = title_rect.midbottom[0] - (menu_btn_bg_rect.width / 2)
menu_btn_bg_rect.y = title_rect.midbottom[1] + BTN_PADDING

menu_btn_txt_rect = menu_btn_txt_surface.get_rect()
menu_btn_txt_rect.x = title_rect.midbottom[0] - (menu_btn_txt_rect.width / 2)
menu_btn_txt_rect.y = title_rect.midbottom[1] + BTN_PADDING + BTN_MARGIN

# === Level One button ===
# Render Level_One btn text onto surface
Level_One_btn_txt_surface = menu_font.render('Level One', True, BLACK)
# Setup Level_One button background
Level_One_btn_bg_rect = Level_One_btn_txt_surface.get_rect()
Level_One_btn_bg_rect.width += 2 * BTN_MARGIN
Level_One_btn_bg_rect.height += 2 * BTN_MARGIN
Level_One_btn_bg_rect.x = (SCREEN_WIDTH / 2) - (0.5 * Level_One_btn_bg_rect.width)
Level_One_btn_bg_rect.y = 50
# Setup the Level_One button text
Level_One_btn_txt_rect = Level_One_btn_txt_surface.get_rect()
Level_One_btn_txt_rect.x = Level_One_btn_bg_rect.x + BTN_MARGIN
Level_One_btn_txt_rect.y = Level_One_btn_bg_rect.y + BTN_MARGIN

# === Level_Two button ===
# Render Level_Two btn text onto surface
Level_Two_btn_txt_surface = menu_font.render('Level Two (not done)', True, BLACK)
# Setup Level_Two button background
Level_Two_btn_bg_rect = Level_Two_btn_txt_surface.get_rect()
Level_Two_btn_bg_rect.width += 2 * BTN_MARGIN
Level_Two_btn_bg_rect.height += 2 * BTN_MARGIN
Level_Two_btn_bg_rect.x = (SCREEN_WIDTH / 2) - (0.5 * Level_Two_btn_bg_rect.width)
Level_Two_btn_bg_rect.y = Level_One_btn_bg_rect.y + (Level_One_btn_bg_rect.height + BTN_PADDING)
# Setup the Level_Two button text
Level_Two_btn_txt_rect = Level_Two_btn_txt_surface.get_rect()
Level_Two_btn_txt_rect.x = Level_Two_btn_bg_rect.x + BTN_MARGIN
Level_Two_btn_txt_rect.y = Level_Two_btn_bg_rect.y + BTN_MARGIN

# === Level Three button ===
# Render quit btn text onto surface
Level_Three_btn_txt_surface = menu_font.render('Level Three (in progress)', True, BLACK)
# Setup quit button background
Level_Three_btn_bg_rect = Level_Three_btn_txt_surface.get_rect()
Level_Three_btn_bg_rect.width += 2 * BTN_MARGIN
Level_Three_btn_bg_rect.height += 2 * BTN_MARGIN
Level_Three_btn_bg_rect.x = (SCREEN_WIDTH / 2) - (0.5 * Level_Three_btn_bg_rect.width)
Level_Three_btn_bg_rect.y = Level_Two_btn_bg_rect.y + (Level_One_btn_bg_rect.height + BTN_PADDING)
# Setup the quit button text
Level_Three_btn_txt_rect = Level_Three_btn_txt_surface.get_rect()
Level_Three_btn_txt_rect.x = Level_Three_btn_bg_rect.x + BTN_MARGIN
Level_Three_btn_txt_rect.y = Level_Three_btn_bg_rect.y + BTN_MARGIN

# === Back Button =======
# Render back btn text onto surface
back_btn_txt_surface = menu_font.render('back', True, BLACK)
# Setup back button background
back_btn_bg_rect = back_btn_txt_surface.get_rect()
back_btn_bg_rect.width += 2 * BTN_MARGIN
back_btn_bg_rect.height += 2 * BTN_MARGIN
back_btn_bg_rect.x = (SCREEN_WIDTH) - (back_btn_bg_rect.width)
back_btn_bg_rect.y = 615 - 50
# Setup the back button text
back_btn_txt_rect = back_btn_txt_surface.get_rect()
back_btn_txt_rect.x = back_btn_bg_rect.x + BTN_MARGIN
back_btn_txt_rect.y = back_btn_bg_rect.y + BTN_MARGIN

#LEVEL ONE INFO
platform_height = 10
screen_rectangle = screen.get_rect()
bottom_platform = pygame.Rect(
            screen_rectangle.left,
            screen_rectangle.bottom - platform_height,
            screen_rectangle.right - screen_rectangle.left,
            platform_height)
level_one_walls = [
    bottom_platform,
    pygame.Rect([100, 520], [400, 10]),
    pygame.Rect([1, 425], [400, 10]),
    pygame.Rect([800, 425], [400, 10]),
    pygame.Rect([800, 425], [10, 190]),
    pygame.Rect([1, 1], [10, 615]),
    pygame.Rect([1190, 1], [10, 613]),
    pygame.Rect([700, 340], [200, 10]),
    pygame.Rect([800, 255], [400, 10]),
    pygame.Rect([1, 255], [500, 10]),
    pygame.Rect([250, 180], [10, 75])]
level_one_exit_rectangle = pygame.Rect([70, 280], [39, 75])
level_one_exit_img = pygame.image.load("exit_redone.png")
level_one_exit_rectangle = level_one_exit_img.get_rect()

target_img = pygame.image.load("portaltarget.png")
target_x = 0
target_y = 0

chell_location_x = 10
chell_location_y = 500
platform_height = 10
platform_color = WHITE
chell_velocity_x = 0 # Larger means moving faster rightwards
chell_velocity_y = 0 # Larger means moving faster downwards
GRAVITATIONAL_CONSTANT = 0.1
is_standing = False

chell_left = pygame.image.load("chell_blue_standingleft.png")
chell_right = pygame.image.load("chell_blue_standing.png")
chell_img = chell_right
chell_rectangle = chell_img.get_rect()

mouse_pos = [0,0]

proj_rect = pygame.rect.Rect(0, 0, 10, 10)
proj_x = 0
proj_y = 0

proj_speed = 8


direction = [0, 0]

blue_portal_rect = pygame.rect.Rect(0, 0, 5, 75)
orange_portal_rect = pygame.rect.Rect(0, 0, 5, 75)

pygame.mixer.music.load("background_music.ogg")
pygame.mixer.music.play(-1, 0.0)

blue_on = False
orange_on = False

portal_timeout = 0.5
last_tele = 0

pygame.mouse.set_visible(True)


##############################################################################
##############################################################################
                # Main Game Loop
##############################################################################
##############################################################################

# Game loop
while True:
    screen.blit(ASCREEN, [0,0])
    # We need to show different things depending on whether or not we're in 'title'
    # or 'menu' mode
    if screen_mode == 'title':
        # ==== TITLE SCREEN MODE ====
        # Draw the title screen
        # Render the title text in the middle of the screen
        screen.blit(title_surface, title_rect)
        # Draw the menu button, first: the text
        pygame.draw.rect(screen, menu_btn_color, menu_btn_bg_rect)
        screen.blit(menu_btn_txt_surface, menu_btn_txt_rect)

    elif screen_mode == 'Levels':
        # === MENU SCREEN MODE ===
        screen.blit(Levels_screen_bg, [0,0])
        # Draw button rectangles!
        # - If button is active, color background with hover color and an outline
        # - otherwise, draw with normal color and no outline
        if Levels_screen_buttons[cur_menu_btn_id] == 'back':
            pygame.draw.rect(screen, menu_btn_hover_color, back_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, back_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, back_btn_bg_rect)

        if Levels_screen_buttons[cur_menu_btn_id] == 'Level_One':
            pygame.draw.rect(screen, menu_btn_hover_color, Level_One_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, Level_One_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, Level_One_btn_bg_rect)


        if Levels_screen_buttons[cur_menu_btn_id] == 'Level_Two':
            pygame.draw.rect(screen, menu_btn_hover_color, Level_Two_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, Level_Two_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, Level_Two_btn_bg_rect)



        if Levels_screen_buttons[cur_menu_btn_id] == 'Level_Three':
            pygame.draw.rect(screen, menu_btn_hover_color, Level_Three_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, Level_Three_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, Level_Three_btn_bg_rect)
        # Layer button text over button backgrounds
        screen.blit(Level_One_btn_txt_surface, Level_One_btn_txt_rect)
        screen.blit(Level_Two_btn_txt_surface, Level_Two_btn_txt_rect)
        screen.blit(Level_Three_btn_txt_surface, Level_Three_btn_txt_rect)
        screen.blit(back_btn_txt_surface, back_btn_txt_rect)
        ########################################################################################################
        # PHYSICAL OUTLOOK OF EACH LEVEL. INSERT CODE BELOW.
        #########################################################################################################

    elif screen_mode == "Level_One":
        screen.fill(BLACK)
        screen.blit(target_img, [target_x, target_y])
        for wall in level_one_walls:
            pygame.draw.rect(screen, WHITE ,wall)

        if blue_on == True:
            pygame.draw.rect(screen, [100, 100, 255], blue_portal_rect)
        if orange_on == True:
            pygame.draw.rect(screen, [255, 165, 0], orange_portal_rect)
        if time.time() - last_tele > portal_timeout and blue_on == True and orange_on == True:
            if chell_rectangle.colliderect(blue_portal_rect):
                chell_rectangle.center = orange_portal_rect.center
                last_tele = time.time()


            elif chell_rectangle.colliderect(orange_portal_rect):
                chell_rectangle.center = blue_portal_rect.center
                last_tele = time.time()


        #Shooting
        if is_shooting == 'Blue'or is_shooting == 'Orange':

            direction = [mouse_pos[0] - chell_rectangle.left, mouse_pos[1] - chell_rectangle.top]
            normal = math.sqrt(direction[0] **2 + direction[1] **2)
            direction[0] /= normal
            direction[1] /= normal

            direction[0] *= proj_speed
            direction[1] *= proj_speed

            proj_x += direction[0]
            proj_y += direction[1]

            proj_rect.x = proj_x
            proj_rect.y = proj_y

            if is_shooting == 'Blue':
                pygame.draw.rect(screen, [100, 100, 255], proj_rect)
            elif is_shooting == 'Orange':
                pygame.draw.rect(screen, [255, 165, 0], proj_rect)

            if proj_rect.collidelist(level_one_walls) != -1:
                if is_shooting == 'Blue':
                    blue_on = True
                    blue_portal_rect.center = proj_rect.center
                else:
                    orange_on = True
                    orange_portal_rect.center = proj_rect.center
                is_shooting = ""


        ############################################################################################################
        #    Player Shooting and Movement
        ############################################################################################################

        if screen_mode == "Level_One" or screen_mode == "Level_Two" or screen_mode == "Level_Three":


            exit_img = pygame.image.load("exit_redone.png")
            exit_rectangle = exit_img.get_rect()
            screen_rectangle = screen.get_rect()
            bottom_platform = pygame.Rect(
            screen_rectangle.left,
            screen_rectangle.bottom - platform_height,
            screen_rectangle.right - screen_rectangle.left,
            platform_height)
            platforms = [bottom_platform]

            is_standing = False
            index = chell_rectangle.collidelist(level_one_walls)
            if index != -1:
                touching_platform = level_one_walls[index]
                is_just_touching_down = chell_rectangle.bottom - touching_platform.top < platform_height

                is_descending = chell_velocity_y > 0
                # is_descending = True

                if is_just_touching_down and is_descending:
                    chell_location_y = touching_platform.top - chell_rectangle.height
                    is_standing = True
                    chell_velocity_y = 0
            # Draw chell (this is the hardest because we need to use chell's
            # x and y location to determine where to place them).

            if chell_rectangle.colliderect(level_one_exit_rectangle):
                screen_mode = "Levels"
                pygame.mouse.set_visible(True)



            if chell_velocity_x >0:
                chell_img = chell_right
            if chell_velocity_x <0:
                chell_img = chell_left
            chell_rectangle.left += chell_velocity_x
            if chell_rectangle.left <= 0:
                chell_rectangle.left = 0
            elif chell_rectangle.right >= SCREEN_WIDTH:
                chell_rectangle.right = SCREEN_WIDTH
            chell_velocity_y += GRAVITATIONAL_CONSTANT
            chell_rectangle.top += chell_velocity_y

            print(chell_rectangle.top, GRAVITATIONAL_CONSTANT)
            if chell_rectangle.top <= 0:
                chell_rectangle.top = 0
            elif chell_rectangle.bottom >= SCREEN_HEIGHT:
                chell_rectangle.bottom = SCREEN_HEIGHT
            screen.blit(chell_img, chell_rectangle)
            screen.blit(level_one_exit_img, level_one_exit_rectangle)

    else:
        # ==== ???? MODE ====
        print("UNRECOGNIZED SCREEN MODE! Exiting.")
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===== TITLE MODE EVENTS =====
        if screen_mode == 'title' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if menu_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'Levels'
                cur_menu_btn_id = 0

        # ===== LEVELS MODE EVENTS =====
        if screen_mode == 'Levels' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'title'
                cur_menu_btn_id = 0
                print("test")
        if screen_mode == 'Levels' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if Level_One_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'Level_One'
                chell_rectangle.top = 500
                cur_menu_btn_id = 0
                print("test")

        if screen_mode == 'Level_One':
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_visible(False)

                mouse_pos = pygame.mouse.get_pos()
                pressed = pygame.mouse.get_pressed()
                if pressed[0] == True:
                    is_shooting = 'Blue'
                elif pressed[2] == True:
                    is_shooting = 'Orange'
                proj_x, proj_y = chell_rectangle.center
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                target_x = x
                target_y = y

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and is_standing:
                # if event.key == pygame.K_UP
                # changing them to make chell jump or run faster.
                chell_velocity_y = -3.9
            if event.key == pygame.K_RIGHT:
                chell_velocity_x = 4
            if event.key == pygame.K_LEFT:
                chell_velocity_x = -4
        # This code ensures that when you release the left or right arrow keys
        # chell stops moving.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                chell_velocity_x = 0
            if event.key == pygame.K_LEFT:
                chell_velocity_x = 0

    clock.tick(FPS)
    pygame.display.update()