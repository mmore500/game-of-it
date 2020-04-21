import sys
import random
import pygame
import itertools


pygame.init()

################################################################
# Colors
crimson = [204, 0, 0]
bla = [0, 0, 0]
darkgrey = [90, 90, 100]
background = [56, 0, 20]
red = [220, 0, 0]
WHITE = [255, 255, 255]
BLACK = [88, 88, 88]
YELLOW = [255, 204, 229] #highlight
menu_btn_color = YELLOW
menu_btn_hover_color = bla
################################################################

screenwidth = 1500
screenheight = 1000
FPS = 60
BTN_PADDING = 10    # How much padding are we going to put around a button?
BTN_MARGIN = 10

gravity = 0.045

screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("Finding Light")
clock = pygame.time.Clock()
menu_font = pygame.font.SysFont('impact', 32)
screen_mode = 'title'   # Modes: title, menu

filenames = itertools.cycle(['sus.ogg', 'jumpy.ogg', 'happy.ogg'])
pygame.mixer.music.load('sus.ogg')
pygame.mixer.music.play(-1)


#################################################################
# title
title_font = pygame.font.SysFont('impact', 128)
title_surface = title_font.render('Finding Light', True, WHITE)
title_rect = title_surface.get_rect()
title_rect.x = (screenwidth / 2) - (title_rect.width / 2) # Put rect in middle of screen (perfectly in middle x)
title_rect.y = (screenheight /2) - (title_rect.height / 2) # Put rect in middle of the screen (sitting on top of horizontal midline)
#Background
loadingscreen_image = pygame.image.load('loadingscreen.png')
loadingscreen_rect = loadingscreen_image.get_rect()
loadingscreen_rect.center = [100, 400]
# === Open menu button ===
menu_btn_txt_surface = menu_font.render('Main Menu', True, BLACK)

menu_btn_bg_rect = menu_btn_txt_surface.get_rect()
#size correctly
menu_btn_bg_rect.width = menu_btn_bg_rect.width + (2*BTN_MARGIN)
menu_btn_bg_rect.height = menu_btn_bg_rect.height + (2*BTN_MARGIN)

#position it
menu_btn_bg_rect.x = (screenwidth / 2) - (menu_btn_bg_rect.width / 2)
menu_btn_bg_rect.y = title_rect.bottom + BTN_PADDING

menu_btn_txt_rect = menu_btn_txt_surface.get_rect()
menu_btn_txt_rect.x = menu_btn_bg_rect.x + BTN_MARGIN
menu_btn_txt_rect.y = menu_btn_bg_rect.y + BTN_MARGIN
#################################################################END SCREEN
catimage = pygame.image.load('cat.png')
catx = 10
caty = 10
endfont = pygame.font.SysFont('impact', 128)
endcolor = [255,255,255]
endsurface = endfont.render("You Lost...",True, endcolor, crimson)
endrect = endsurface.get_rect()
endx = (screenwidth / 2 ) - (endrect.width / 2)
endy = (screenheight / 2 ) - (endrect.height / 2)
backrect = pygame.Rect(400, 375, 700, 250)
###############################################################WIN SCREEN
winimage = pygame.image.load('win.png')
winfont = pygame.font.SysFont('impact', 128)
wincolor = [255,255,255]
winsurface = winfont.render("You Won!",True, wincolor,)
winrect = winsurface.get_rect()
winx = (screenwidth / 2 ) - (winrect.width / 2)
winy = (screenheight / 2 ) - (winrect.height / 2)
winimage = pygame.image.load('win.png')
winimage_rect = winimage.get_rect()
#################################################################
# menu
menu_screen_buttons = ['quit', 'resume'] # Available buttons
cur_menu_btn_id = 0                                # What button are we currently on?
btn_color = YELLOW

# === Resume button ===
# Render resume btn text onto surface
resume_btn_txt_surface = menu_font.render('Start Game', True, BLACK)
# Setup resume button background
resume_btn_bg_rect = resume_btn_txt_surface.get_rect()
resume_btn_bg_rect.width += 2 * BTN_MARGIN
resume_btn_bg_rect.height += 2 * BTN_MARGIN
resume_btn_bg_rect.x = (screenwidth / 2) - (resume_btn_bg_rect.width / 2)
resume_btn_bg_rect.y = 400
# Setup the resume button text
resume_btn_txt_rect = resume_btn_txt_surface.get_rect()
resume_btn_txt_rect.x = resume_btn_bg_rect.x + BTN_MARGIN
resume_btn_txt_rect.y = resume_btn_bg_rect.y + BTN_MARGIN

# === Quit button ===
# Render quit btn text onto surface
quit_btn_txt_surface = menu_font.render('Quit', True, BLACK)
# Setup quit button background
quit_btn_bg_rect = quit_btn_txt_surface.get_rect()
quit_btn_bg_rect.width += 2 * BTN_MARGIN
quit_btn_bg_rect.height += 2 * BTN_MARGIN
quit_btn_bg_rect.x = resume_btn_bg_rect.x + (resume_btn_bg_rect.width / 4)
quit_btn_bg_rect.y = resume_btn_bg_rect.y + (resume_btn_bg_rect.y / 4)
# Setup the quit button text
quit_btn_txt_rect = quit_btn_txt_surface.get_rect()
quit_btn_txt_rect.x = quit_btn_bg_rect.x + BTN_MARGIN
quit_btn_txt_rect.y = quit_btn_bg_rect.y + BTN_MARGIN
################################################################################

#################################################################
# game

loadingscreengame_image = pygame.image.load('back.png')
loadingscreengame_rect = loadingscreengame_image.get_rect()
loadingscreengame_rect.center = [screenwidth/2, screenheight / 2]


standing = False
win = False
health = 1

back_image = pygame.image.load('back.png')

charimage = pygame.image.load('sprite.png')
char_rect = charimage.get_rect()

char_velocity_x = 0
char_velocity_y = 0
catx = 10
caty = 10
charheight = 75
charwidth = 25
char_rect.left = 0
char_rect.top = 0

death_blocks = [
    pygame.Rect(200, 0, 60, 220),
    pygame.Rect(800, 0, 60, 175),
    pygame.Rect(970, 300, 360, 15),
    pygame.Rect(0, 420, 190, 60),
    pygame.Rect(450, 0, 15, 600),
    pygame.Rect(300, 850, 15, 100),
    pygame.Rect(800, 800, 30, 300),
    pygame.Rect(1313, 170, 30, 400),
    pygame.Rect(1300, 600, 30, 300),
    pygame.Rect(1250, 400, 30, 300),
    pygame.Rect(700, 500, 300, 30),
    pygame.Rect(450, 620, 200, 30),
    pygame.Rect(0, 800, 30, 15)]

end_block = pygame.image.load('bloss.png')
end_block_rect = end_block.get_rect()
end_block_rect.x = screenwidth - end_block_rect.width
end_block_rect.y = 500
platforms = [
    pygame.Rect(200, 620, 250, 15),
    pygame.Rect(800, 800, 300, 15),
    pygame.Rect(600, 300, 300, 15),
    pygame.Rect(1, 940, 2000, 65)]

while True:
    # We need to show different things depending on whether or not we're in 'title'
    # or 'menu' mode
    if screen_mode == 'title':
        # ==== TITLE SCREEN MODE ====
        screen.fill(bla)
        loadingscreen_image = pygame.image.load('loadingscreen.png')
        loadingscreen_rect = loadingscreen_image.get_rect()
        loadingscreen_rect.center = [screenwidth  / 2, screenheight / 2]
        screen.blit(loadingscreen_image, loadingscreen_rect)
        # Draw the title screen
        # Render the title text in the middle of the screen
        screen.blit(title_surface, title_rect)
        # Draw the menu button, first: the text
        pygame.draw.rect(screen, menu_btn_color, menu_btn_bg_rect)
        screen.blit(menu_btn_txt_surface, menu_btn_txt_rect)

    elif screen_mode == 'menu':
        # === MENU SCREEN MODE ===
        screen.fill(bla)
        loadingscreen_image = pygame.image.load('loadingscreen.png')
        loadingscreen_rect = loadingscreen_image.get_rect()
        loadingscreen_rect.center = [screenwidth / 2, screenheight / 2]
        screen.blit(loadingscreen_image, loadingscreen_rect)

        # Draw button rectangles!
        # - If button is active, color background with hover color and an outline
        # - otherwise, draw with normal color and no outline
        #print(cur_menu_btn_id)
        if menu_screen_buttons[cur_menu_btn_id] == 'resume':
            pygame.draw.rect(screen, menu_btn_hover_color, resume_btn_bg_rect)#draw menu box
            pygame.draw.rect(screen, bla, resume_btn_bg_rect, 5)#draw outline
        else:
            pygame.draw.rect(screen, menu_btn_color, resume_btn_bg_rect)
        if menu_screen_buttons[cur_menu_btn_id] == 'quit':
            pygame.draw.rect(screen, menu_btn_hover_color, quit_btn_bg_rect)
            pygame.draw.rect(screen, bla, quit_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, quit_btn_bg_rect)

        # Layer button text over button backgrounds
        screen.blit(resume_btn_txt_surface, resume_btn_txt_rect)

        screen.blit(quit_btn_txt_surface, quit_btn_txt_rect)
    elif screen_mode == 'game':
        standing = False
        platform_index = char_rect.collidelist(platforms)
        if platform_index != -1:
            platform = platforms[platform_index]
            is_just_touching_down = char_rect.bottom - platform.top < platform.height
            is_descending = char_velocity_y > 0

            if is_just_touching_down and is_descending:
                char_rect.top = platform.top - char_rect.height
                standing = True
                char_velocity_y = 1

        if char_rect.collidelist(death_blocks) != -1:
            health = 0

        if char_rect.colliderect(end_block_rect):
            win = True
            print("you won")
            ###############################################NEED TO DO
            screen_mode = 'winscreen'
            continue

        screen.blit(loadingscreengame_image, loadingscreengame_rect)
        for death_block in death_blocks:
            pygame.draw.rect(screen,red,death_block)
        for platform in platforms:
            pygame.draw.rect(screen, darkgrey, platform)
        screen.blit(end_block, end_block_rect)
        screen.blit(charimage, char_rect)

        if health == 0:

            print("U DED")
           # pygame.quit()
            #sys.exit()
            screen_mode = 'gameover'


        char_rect.left += char_velocity_x
        char_rect.top += char_velocity_y

        char_velocity_x *= 0.99
        char_velocity_y *= 0.99
        char_velocity_y += gravity

    elif screen_mode == 'gameover':
        screen.fill(bla)
        for i in range(300):
            screen.blit(catimage, [random.randint(0, screenwidth), random.randint(0, screenheight)])
            catx = catx + 1
            pygame.draw.rect(screen, crimson, backrect)
            screen.blit(endsurface, [endx, endy])

        # ===== WIN SCREEN =============
    elif screen_mode == 'winscreen':
            screen.fill(bla)
            winimage_rect.center = [screenwidth / 2, screenheight / 2]
            screen.blit(winimage, [0,0])

            screen.blit(winsurface, [winx, winy])


    else:
        # ==== ???? MODE ====
        print("AAAH UNRECOGNIZED SCREEN MODE! Exiting")
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
                screen_mode = 'menu'
                cur_menu_btn_id = 0

        # ===== MENU MODE EVENTS =====
        if screen_mode == 'menu' and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # player presses down arrow
                cur_menu_btn_id = (cur_menu_btn_id + 1) % len(menu_screen_buttons)
            if event.key == pygame.K_UP:
                # player presses up arrow
                cur_menu_btn_id = (cur_menu_btn_id - 1) % len(menu_screen_buttons)
            if event.key == pygame.K_RETURN:
                # Player presses return (selects current option)
                if menu_screen_buttons[cur_menu_btn_id] == 'quit':
                    # if on resume button, go back to title screen
                     screen_mode = 'game'

                    #Need to direct to game

                elif menu_screen_buttons[cur_menu_btn_id] == 'resume':
                    # if on quit button, quit the game

                    pygame.quit()
                    sys.exit()
        if screen_mode == 'game':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                      print("Space key press.")

                      #Shooter
                elif event.key == pygame.K_w:
                    print("w key was pressed")
                    char_velocity_y -= 1
                elif event.key == pygame.K_s:
                    print("s key was pressed")
                    char_velocity_y += 1
                elif event.key == pygame.K_a:
                    print("a key was pressed")
                    char_velocity_x -= 1
                elif event.key == pygame.K_d:
                    print("d key was pressed")
                    char_velocity_x += 1
    clock.tick(FPS)
    pygame.display.update()