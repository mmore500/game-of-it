#Game Code

import sys
import pygame


FPS = 60
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

BTN_PADDING = 10    # How much padding are we going to put around a button?
BTN_MARGIN = 10     # How much space do we want around button text?


#Colors
WHITE = [255, 255, 255]
ANTI_WHITE = [236, 239, 241]
LIGHT_GREY = [207, 216, 219]

#Mid-Shades
LIGHT_S_GREY = [120, 144, 156]

#Dark Colors
CHARCOAL = [55, 71, 79]

pygame.init()

pygame.mixer.music.load('dead_silence_theme.mp3')
pygame.mixer.music.play(-1) 

GHOST_png = pygame.image.load('GHOST.png')
GHOST_png = pygame.transform.scale(GHOST_png, (100,100))

GRIMM_png = pygame.image.load('GRIMM.png')
GRIMM_png = pygame.transform.scale(GRIMM_png, (100,100))

MSG_png = pygame.image.load('MSG (2).png')
GHOST_x = 10
GHOST_y = 10
SPEED = 5

BACKGROUND_png = pygame.image.load('BACKGROUND.png')


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
settings_font = pygame.font.SysFont('impact', 64)   # Here's our button font
print("Loaded the font!")
screen_mode = 'INTRO'   # Modes: intro, menu


NEW_ICON_png = pygame.image.load('NEW_ICON.png')
NEW_ICON_png = pygame.transform.scale(NEW_ICON_png, (256, 256))
NEW_ICON_rect = NEW_ICON_png.get_rect()
NEW_ICON_rect.x = (SCREEN_WIDTH / 2) - (NEW_ICON_rect.width / 2)
NEW_ICON_rect.y = (SCREEN_HEIGHT / 2) - NEW_ICON_rect.height

SCROLLER_png = pygame.image.load('ICONS/SCROLLER.png')
SCROLLER_png = pygame.transform.scale(SCROLLER_png, (64, 64))

TOMATO_png = pygame.image.load('TOMATO.png')
TOMATO_png = pygame.transform.scale(TOMATO_png, (32, 32))

LETTUCE_png = pygame.image.load('LETTUCE.png')
LETTUCE_png = pygame.transform.scale(LETTUCE_png, (32, 32))


play_text = settings_font.render("Start" , True, LIGHT_S_GREY)
play_rect = play_text.get_rect()
play_rect.x = (SCREEN_WIDTH / 2) - (play_rect.width / 2)
play_rect.y = (SCREEN_HEIGHT / 2) - play_rect.height + 100

scrolls = [
    {"img":SCROLLER_png, "goto": "GAME", "collected": False, "x": 300, "y": 400,"screen_mode": "GAME","msg": " Welcome player, Here's a little welcome gift to get you started; 3 Hearts, 2 Fireballs, Starter Scroll. Be wise about your choices from here on out. Good Luck on your journey! - F"},
    {"img":SCROLLER_png,"goto": "CRYPT", "collected": False, "x": 230, "y": 200, "screen_mode": "GAME","msg": " Congratulations! you have found your first scroll, there will be many more through out the game. Hopefully you will find them all. Good luck player on your journey!"},  
    {"img":GRIMM_png, "goto":"INTRO", "collected": False,"x": 0, "y": 0, "screen_mode": "CRYPT","msg": "..."},
    {"img":SCROLLER_png, "goto": "CRYPT", "collected" : False, "x": 25, "y": 400,"screen_mode": "CRYPT", "msg": "Beware of Grimm...-F"},
    {"img":TOMATO_png, "goto": "INTRO", "collected": False, "x": 362, "y":362, "screen_mode": "CRYPT", "msg": "Ouch!"}
    ]

setting_btn_color = ANTI_WHITE
setting_btn_hover_color = LIGHT_GREY

#TITLE SCREEN
title_screen_bg_color = LIGHT_GREY


setting_btn_txt_surface = settings_font.render('Settings', True, LIGHT_S_GREY)

setting_btn_bg_rect = setting_btn_txt_surface.get_rect()
setting_btn_bg_rect.width += 2 * BTN_MARGIN  # Add some margins to the button
setting_btn_bg_rect.height += 2 * BTN_MARGIN # Add margin to the button

setting_btn_bg_rect.x = NEW_ICON_rect.midbottom[0] - (setting_btn_bg_rect.width / 2)
setting_btn_bg_rect.y = NEW_ICON_rect.midbottom[1] + BTN_PADDING + BTN_MARGIN


#SETTING COMP
setting_screen_bg_color = CHARCOAL

setting_screen_buttons = ['Mute', 'Quit', 'Back to Home'] # Available buttons
cur_setting_btn_id = 0                    
btn_color = LIGHT_GREY

#SETTING BTN
setting_btn_txt_surface = settings_font.render('Settings', True, LIGHT_S_GREY)

# Setup Setting menu button background
setting_btn_bg_rect = setting_btn_txt_surface.get_rect()
setting_btn_bg_rect.width = setting_btn_bg_rect.width + (2*BTN_MARGIN)
setting_btn_bg_rect.height = setting_btn_bg_rect.height + (2*BTN_MARGIN)
setting_btn_bg_rect.x = (SCREEN_WIDTH /2) - (setting_btn_bg_rect.width / 2)
setting_btn_bg_rect.y = 0 #title_rect.bottom

# Setup txt rect
setting_btn_txt_rect = setting_btn_txt_surface.get_rect()
setting_btn_txt_rect.x = setting_btn_bg_rect.x + BTN_MARGIN
setting_btn_txt_rect.y = setting_btn_bg_rect.y + BTN_MARGIN



while True:

    
    if screen_mode == 'INTRO':
        for scroll in scrolls:
            scroll["collected"] = False
            if scroll["img"] == GRIMM_png:
                scroll["x"] = 0
                scroll["y"] = 0
        GHOST_x = (SCREEN_WIDTH / 2) - 100
        GHOST_y = SCREEN_HEIGHT - 100
        # ==== TITLE SCREEN MODE ====
        screen.fill(title_screen_bg_color)
        screen.blit(NEW_ICON_png, NEW_ICON_rect)
        pygame.draw.rect(screen, ANTI_WHITE, play_rect) 
        screen.blit(play_text, play_rect)
          
    
    elif screen_mode == 'Settings':
        # === MENU SCREEN MODE ===
        screen.fill(setting_screen_bg_color)
        if setting_screen_buttons[cur_setting_btn_id] == 'Mute':
            pygame.draw.rect(screen, setting_btn_hover_color, setting_btn_bg_rect)
            pygame.draw.rect(screen, CHARCOAL, setting_btn_bg_rect, 5)
 

        screen.blit(setting_btn_txt_surface)

    elif screen_mode == "GAME":
        screen.fill(WHITE)
        BLACK = [0, 0, 0] 
        screen.fill(BLACK)
        screen.blit(BACKGROUND_png, (0, 0))
        
    elif screen_mode == "CRYPT":
        screen.fill(LIGHT_S_GREY)
        for scroll in scrolls :
            if scroll["img"] == GRIMM_png:
                scroll["x"] = (GHOST_x + scroll["x"] * 99) / 100
                scroll["y"] = (GHOST_y + scroll["y"] * 99) / 100
    
    
    else:
        print("unknown.")



    if screen_mode == "CRYPT" or screen_mode == "GAME":
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT] and not pressed_keys[pygame.K_LEFT]:
            GHOST_x = (GHOST_x + SPEED) % SCREEN_WIDTH
        elif pressed_keys[pygame.K_LEFT] and not pressed_keys[pygame.K_RIGHT]:
            GHOST_x = (GHOST_x - SPEED) % SCREEN_WIDTH
      
        if pressed_keys[pygame.K_UP] and not pressed_keys[pygame.K_DOWN]:
            GHOST_y = (GHOST_y - SPEED) % SCREEN_HEIGHT
        elif pressed_keys[pygame.K_DOWN] and not pressed_keys[pygame.K_UP]:
            GHOST_y = (GHOST_y + SPEED) % SCREEN_HEIGHT
        
        screen.blit(GHOST_png, [GHOST_x, GHOST_y])
        
    ghost_rect = GHOST_png.get_rect()
    ghost_rect.x = GHOST_x
    ghost_rect.y = GHOST_y
    for scroll in scrolls:
        scroll_rect = scroll["img"].get_rect()
        scroll_rect.x = scroll["x"]
        scroll_rect.y = scroll["y"]
        if scroll["screen_mode"] == screen_mode and not scroll["collected"]:
            screen.blit(scroll["img"], [scroll["x"], scroll["y"]])
            if ghost_rect.colliderect(scroll_rect):
                scroll["collected"]= True
                print("=" * 20)
                print(scroll["msg"]) 
                print("=" * 20)
                screen_mode = scroll["goto"]
                
            for other in scrolls:
                other_rect = other["img"].get_rect()
                other_rect.x = other["x"]
                other_rect.y = other["y"]
                if other["img"] == scroll["img"]:
                    continue
                elif other["img"] == TOMATO_png and other_rect.colliderect(scroll_rect):
                    scroll["collected"] = True
                    print("OUCH! It burns!")
                    print("You coming too?")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and screen_mode == "INTRO":
            print("test") 
            mouse_pos = pygame.mouse.get_pos() 
            if play_rect.collidepoint(mouse_pos):
                screen_mode = 'GAME'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               pass
            elif event.key == pygame.K_UP:
               GHOST_y -= + SPEED
            elif event.key == pygame.K_LEFT:
               GHOST_x -= + SPEED
            elif event.key == pygame.K_DOWN:
               GHOST_y -= - SPEED
            elif event.key == pygame.K_RIGHT:
               GHOST_x -= - SPEED
              
        # ===== TITLE MODE EVENTS =====
        
          

    clock.tick(FPS)
    pygame.display.update()








