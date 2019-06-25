'''
Block catchy game with all the bells and whistles(?), maybe
'''

import sys
import random
import pygame

# CONSTANTS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60
BTN_MARGIN = 5

CATCHER_WIDTH = 100
CATCHER_HEIGHT = 25
CATCHER_SPEED = 10
CATCHER_START_HEALTH = 2

OBJ_SPAWN_CHANCE = 0.2
CHANCE_SPAWN_IS_GOOD = 0.25
OBJ_SPEED = 5

BAD_OBJECT_WIDTH = 10
BAD_OBJECT_HEIGHT = 10
BAD_OBJECT_DMG = 1

GOOD_OBJECT_WIDTH = 10
GOOD_OBJECT_HEIGHT = 10
BAD_OBJECT_WIDTH = 10
BAD_OBJECT_HEIGHT = 10

RED = [255, 0, 0]
LIGHT_GREY = [230, 230, 230]
BLACK = [0, 0, 0]
BLUE = [0,0,230]
WHITE = [255, 255, 255]
YELLOW = [255, 229, 153]

# Initial setup
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("EXTREME BLOCK CATCHING")
clock = pygame.time.Clock()

game_screens = ['title', 'play', 'end']
cur_game_screen = 'title'

title_bg_color = BLACK
play_bg_color = LIGHT_GREY
end_bg_color = BLACK
button_color = YELLOW

title_font = pygame.font.SysFont('impact', 64)
button_font = pygame.font.SysFont('impact', 18)
game_info_font = pygame.font.SysFont('impact', 24)
################################################################################
# Title screen components
################################################################################
title_screen_bg_color = BLACK
# Title text
title_surface = title_font.render('2 FAST 2 CATCH BLOCKS', True, WHITE)
title_rect = title_surface.get_rect()
title_rect.x = (SCREEN_WIDTH / 2) - (title_rect.width / 2) # Put rect in middle of screen (perfectly in middle x)
title_rect.y = (SCREEN_HEIGHT / 2) - (title_rect.height)   # Put rect in middle of the screen (sitting on top of horizontal midline)

# Play button
play_btn_txt_surface = button_font.render('>>>> CATCH BLOCKS <<<<', True, BLACK)
# setup play button background
play_btn_bg_rect = play_btn_txt_surface.get_rect()
play_btn_bg_rect.width += 2 * BTN_MARGIN  # Add some margins to the button
play_btn_bg_rect.height += 2 * BTN_MARGIN # Add margin to the button
play_btn_bg_rect.x = title_rect.midbottom[0] - (play_btn_bg_rect.width / 2)
play_btn_bg_rect.y = title_rect.midbottom[1]
# setup play button text
play_btn_txt_rect = play_btn_txt_surface.get_rect()
play_btn_txt_rect.x = play_btn_bg_rect.x + BTN_MARGIN
play_btn_txt_rect.y = play_btn_bg_rect.y + BTN_MARGIN

################################################################################
# Play screen components
################################################################################

catcher_start_x = (SCREEN_WIDTH / 2) - (CATCHER_WIDTH / 2)
catcher_start_y = SCREEN_HEIGHT - CATCHER_HEIGHT - 1
catcher = pygame.Rect([catcher_start_x, catcher_start_y], [CATCHER_WIDTH, CATCHER_HEIGHT])
falling_objects = []

# bomb_img = pygame.image.load('bomb-small.png') # Challenge: use bomb img instead of red squares

health = CATCHER_START_HEALTH
score = 0

################################################################################
# End screen components
################################################################################

# game over
game_over_txt = title_font.render('GAME OVER', True, BLACK)
game_over_rect = game_over_txt.get_rect()
game_over_rect.x = (SCREEN_WIDTH / 2) - (game_over_rect.width / 2) # Put rect in middle of screen (perfectly in middle x)
game_over_rect.y = (SCREEN_HEIGHT / 2) - (game_over_rect.height)   # Put rect in middle of the screen (sitting on top of horizontal midline)

# Replay button
replay_btn_txt = game_info_font.render('PLAY AGAIN?', True, BLACK)
# setup play button background
replay_btn_bg_rect = replay_btn_txt.get_rect()
replay_btn_bg_rect.width += 2 * BTN_MARGIN  # Add some margins to the button
replay_btn_bg_rect.height += 2 * BTN_MARGIN # Add margin to the button
replay_btn_bg_rect.x = game_over_rect.midbottom[0] - (replay_btn_bg_rect.width / 2)
replay_btn_bg_rect.y = game_over_rect.midbottom[1]
# setup play button text
replay_btn_txt_rect = replay_btn_txt.get_rect()
replay_btn_txt_rect.x = replay_btn_bg_rect.x + BTN_MARGIN
replay_btn_txt_rect.y = replay_btn_bg_rect.y + BTN_MARGIN

while True:

    if cur_game_screen == 'title':
        screen.fill(title_bg_color)
        # Draw the title
        screen.blit(title_surface, title_rect)
        # Draw the play button
        pygame.draw.rect(screen, button_color, play_btn_bg_rect)
        screen.blit(play_btn_txt_surface, play_btn_txt_rect)

    elif cur_game_screen == 'play':
        screen.fill(play_bg_color)

        # Use arrow keys to control the catcher
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT] and not pressed_keys[pygame.K_LEFT]:
            catcher.x = (catcher.x + CATCHER_SPEED) % SCREEN_WIDTH
        elif pressed_keys[pygame.K_LEFT] and not pressed_keys[pygame.K_RIGHT]:
            catcher.x = (catcher.x - CATCHER_SPEED) % SCREEN_WIDTH

        # Draw falling rocks
        spawn_new_falling_object = len(falling_objects) == 0 or (random.random() < OBJ_SPAWN_CHANCE)
        if spawn_new_falling_object:
            # Good or bad object?
            obj_good = random.random() < CHANCE_SPAWN_IS_GOOD
            if obj_good:
                # obj is friendly
                new_obj_rect = pygame.Rect([random.randint(GOOD_OBJECT_WIDTH, SCREEN_WIDTH - 2*GOOD_OBJECT_WIDTH), 0], [GOOD_OBJECT_WIDTH, GOOD_OBJECT_HEIGHT])
                falling_objects.append({"rect": new_obj_rect, "good": True})
            else:
                # obj is EVIL
                new_obj_rect = pygame.Rect([random.randint(BAD_OBJECT_WIDTH, SCREEN_WIDTH - 2*BAD_OBJECT_WIDTH), 0], [BAD_OBJECT_WIDTH, BAD_OBJECT_HEIGHT])
                falling_objects.append({"rect": new_obj_rect, "good": False})

        # Draw objects
        on_screen_objs = []
        for obj in falling_objects:
            obj["rect"].y += OBJ_SPEED
            color = BLUE if obj["good"] else RED

            pygame.draw.rect(screen, color, obj["rect"])

            if catcher.colliderect(obj["rect"]):
                # Collision!
                if obj["good"]:
                    score += 1
                else:
                    health -= BAD_OBJECT_DMG
                print("Health =", health, "Score =", score)
            elif obj["rect"].y < SCREEN_HEIGHT:
                on_screen_objs.append(obj)

        falling_objects = on_screen_objs


        # Draw the catcher rectangle
        pygame.draw.rect(screen, BLACK, catcher)

        # Draw game info
        health_surface = game_info_font.render('HEALTH: ' + str(health), True, BLACK)
        health_rect = health_surface.get_rect()
        health_rect.x = SCREEN_WIDTH - health_rect.width - 50
        health_rect.y = 50
        screen.blit(health_surface, health_rect)

        score_surface = game_info_font.render('SCORE: ' + str(score), True, BLACK)
        score_rect = score_surface.get_rect()
        score_rect.x = SCREEN_WIDTH - score_rect.width - 50
        score_rect.y = health_rect.bottom + 50
        screen.blit(score_surface, score_rect)

        # End game state
        if health == 0:
            cur_game_screen = 'end'

    elif cur_game_screen == 'end':
        # screen.fill(end_bg_color)
        screen.blit(game_over_txt, game_over_rect)

        pygame.draw.rect(screen, button_color, replay_btn_bg_rect)
        screen.blit(replay_btn_txt, replay_btn_txt_rect)


    # setup the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if cur_game_screen == 'title':
            # Title screen events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_btn_bg_rect.collidepoint(mouse_pos):
                    cur_game_screen = 'play'
        if cur_game_screen == 'end':
            # End game screen events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if replay_btn_bg_rect.collidepoint(mouse_pos):
                    cur_game_screen = 'title'
                    score = 0
                    health = CATCHER_START_HEALTH
                    falling_objects = []
                    catcher.x = catcher_start_x
                    catcher.y = catcher_start_y

    pygame.display.update()
    clock.tick(FPS)
