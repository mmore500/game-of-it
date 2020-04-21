import sys
import random
import pygame
import itertools
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

BTN_PADDING = 10    # How much padding are we going to put around a button?
BTN_MARGIN = 10     # How much space do we want around button text?


RED = [255, 0, 0]
ORANGE = [ 255, 127, 0]
YELLOW = [255, 255,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
INDIGO = [39, 0, 51]
VIOLET = [139, 0, 255]
LIGHT_GREY = [230, 230, 230]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
DARKER_YELLOW = [255, 217, 102]
GREY = [175, 175, 175]


uw = 10
uh = 10
usx = 1100
usy = 700
us = 5

userHP = 50
tot_userHP = 50
user_color = RED
alreadyused = True

cuxv = 0
cuyv = 0
user = pygame.Rect([usx,usy],[uw,uh])

bullets = []
bvx = 10
bw = 7.5
bh = 5
absolute_speed = 10
bulletife = 10

tw = 20
th = 20
ts = 2
'''
bdamage =
bhealth =
bmaxhealth =

'''
print('Available fonts:', pygame.font.get_fonts())



pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("RISING THROUGH THE RAINBOW")
clock = pygame.time.Clock()



menu_font = pygame.font.SysFont('impact', 32)   # Here's our button font
print("Loaded the font!")
screen_mode = 'title'   # Modes: title, menu

menu_btn_color = YELLOW
menu_btn_hover_color = DARKER_YELLOW

################################################################################
# Title screen components
################################################################################
title_screen_bg_color = BLACK
# === Title text ===
title_font = pygame.font.SysFont('impact', 70)
title_surface = title_font.render('RISING THROUGH THE RAINBOW', True, WHITE)
title_rect = title_surface.get_rect()
title_rect.x = (SCREEN_WIDTH/2) - (title_rect.width/2)# Put rect in middle of screen (perfectly in middle x)
title_rect.y = (SCREEN_HEIGHT/2) - (title_rect.height/2) # Put rect in middle of the screen (sitting on top of horizontal midline)

# === Open menu button ===
menu_btn_txt_surface = menu_font.render('open menu', True, BLACK)

menu_btn_bg_rect= menu_btn_txt_surface.get_rect()

menu_btn_bg_rect.width=menu_btn_bg_rect.width+ (2*BTN_MARGIN)
menu_btn_bg_rect.height=menu_btn_bg_rect.height+(2*BTN_MARGIN)

menu_btn_bg_rect.x = (SCREEN_WIDTH/2) - (menu_btn_bg_rect.width/2)
menu_btn_bg_rect.y = title_rect.bottom 

menu_btn_txt_rect = menu_btn_txt_surface.get_rect()
menu_btn_txt_rect.x = menu_btn_bg_rect.x + BTN_MARGIN
menu_btn_txt_rect.y = menu_btn_bg_rect.y + BTN_MARGIN

################################################################################
# Menu screen components
################################################################################
menu_screen_bg_color = GREY

menu_screen_buttons = ['Instructions', 'Arena', 'quit'] # Available buttons
cur_menu_btn_id = 0                                # What button are we currently on?
btn_color = YELLOW

# === Resume button ===
# Render resume btn text onto surface
resume_btn_txt_surface = menu_font.render('Instructions', True, BLACK)
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

# === Random button ===
# Render random btn text onto surface
random_btn_txt_surface = menu_font.render('Arena', True, BLACK)
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

# === Quit button ===
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
################################################################################
#Instruction Screen Components

#Instruction Text
Instruct_font = pygame.font.SysFont('impact', 70)
Instruct_surface = title_font.render('RISING THROUGH THE RAINBOW', True, WHITE)
Instruct_rect = title_surface.get_rect()
Instruct_rect.x = (SCREEN_WIDTH/2) - (title_rect.width/2)# Put rect in middle of screen (perfectly in middle x)
Instruct_rect.y = (SCREEN_HEIGHT/2) - (title_rect.height/2) # Put rect in middle of the screen (sitting on top of horizontal midline)

back_btn_txt_surface = menu_font.render('back', True, BLACK)

back_btn_bg_rect= menu_btn_txt_surface.get_rect()

back_btn_bg_rect.width=menu_btn_bg_rect.width+ (2*BTN_MARGIN)
back_btn_bg_rect.height=menu_btn_bg_rect.height+(2*BTN_MARGIN)

back_btn_bg_rect.x = (SCREEN_WIDTH/2) - (menu_btn_bg_rect.width/2)
back_btn_bg_rect.y = title_rect.bottom 

back_btn_txt_rect = menu_btn_txt_surface.get_rect()
back_btn_txt_rect.x = menu_btn_bg_rect.x + BTN_MARGIN
back_btn_txt_rect.y = menu_btn_bg_rect.y + BTN_MARGIN

#Arenabox

arena_box_rect = (20,20,1160,760)

#targets
targets = []
total_targets = []
dead_targets = []
directions = []
target_color = RED
for i in range(0,0):
    rand_x = random.randint(0,SCREEN_WIDTH-tw-30)
    rand_y = random.randint(0,SCREEN_HEIGHT-th-30)
    targets.append(pygame.Rect([rand_x,rand_y],[tw,th]))
    total_targets.append(pygame.Rect([rand_x,rand_y],[tw,th]))
print(len(targets),len(directions))
frame = 0
aim = 0

# Game loop
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
        if menu_screen_buttons[cur_menu_btn_id] == 'Instructions':
            pygame.draw.rect(screen, menu_btn_hover_color, resume_btn_bg_rect)
            pygame.draw.rect(screen, BLACK, resume_btn_bg_rect, 5)
        else:
            pygame.draw.rect(screen, menu_btn_color, resume_btn_bg_rect)

        if menu_screen_buttons[cur_menu_btn_id] == 'Arena':
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
    elif screen_mode == 'Instructions':
        screen.fill(menu_screen_bg_color)
        screen.blit(Instruct_surface, Instruct_rect)
        pygame.draw.rect(screen, menu_btn_color, back_btn_bg_rect)
        screen.blit(back_btn_txt_surface, back_btn_txt_rect)
    
    elif screen_mode == 'Arena1':
        screen.fill([247,197,143])
        pygame.draw.rect(screen, BLACK, arena_box_rect)
        HP_font = pygame.font.SysFont('impact', 42)
        HP = HP_font.render('Health: ' + str(userHP), True, user_color)
        HP_rect = HP.get_rect()
        HP_rect.x = 950
        HP_rect.y = 50
        DEATH_font = pygame.font.SysFont('impact', 42)
        DEATH = HP_font.render('Kills: ' + str(len(dead_targets)), True, user_color)
        DEATH_rect = HP.get_rect()
        DEATH_rect.x = 950
        DEATH_rect.y = 100
        screen.blit(HP,HP_rect)
        screen.blit(DEATH,DEATH_rect)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            print("up arrow")
            cuyv = -1*us
        elif pressed_keys[pygame.K_DOWN]:
            print("down arrow")
            cuyv = us
        else:
            cuyv = 0
        if pressed_keys[pygame.K_RIGHT]:
            print("right arrow")
            cuxv = us
        elif pressed_keys[pygame.K_LEFT]:
            print("LEFT!!!!")
            cuxv = -1*us
        else:
            cuxv = 0

        user.left += cuxv
        user.top += cuyv
        pygame.draw.rect(screen, user_color, user)
        usx,usy = user.topleft
        aim_y = absolute_speed * math.sin(aim * (math.pi / 180))
        aim_x = -1 * (absolute_speed * math.cos(aim * (math.pi / 180)))
        pygame.draw.line(screen, user_color,[usx,usy],[usx+aim_x,usy+aim_y])
        
        for target in targets:
            if user.colliderect(target):
                userHP = userHP - 1
                print("HP:",userHP)
                if userHP <= 0:
                    screen_mode = 'title'
                    userHP = 50
                    targets = []
                    dead_targets = []
                    
        
        on_screen_bullets=[]
        for bullet_rect, bullet_x_vel, bullet_y_vel, bullet_life in bullets:
            bullet_rect.left += bullet_x_vel
            bullet_rect.top += bullet_y_vel
            pygame.draw.rect(screen,RED,bullet_rect)
                   #insert enemy death count here
            alive_targets = []
            for target in targets:
                if bullet_rect.colliderect(target):
                    dead_targets.append(target)
                    print("Deaths:",len(dead_targets))
                    print(random.choice(["AAAAHHHH","GRUNT", "UUUGGG", "SPLAT", "POP"]))
                    continue
                alive_targets.append(target)
               
            targets = alive_targets
        
            
 
            if bullet_rect.left <= SCREEN_WIDTH and bullet_life > 0:
                on_screen_bullets.append((bullet_rect, bullet_x_vel, bullet_y_vel, bullet_life - 1))
        bullets = on_screen_bullets
        
        for i in range(0, len(targets)):
            
            if directions[i][0] == 0 or targets[i].y < 100:
                targets[i].y =  targets[i].y + ts
            else:
                targets[i].y = targets[i].y - ts
            
            
            if directions[i][1] == 0 or targets[i].x < 100:
                targets[i].x =  targets[i].x + ts
            else:
                targets[i].x = targets[i].x - ts
            pygame.draw.rect(screen, target_color, targets[i])
                
        if frame % 50 == 0:
            direction = random.randint(0,1)
            direction1 = random.randint(0,1)
            target = pygame.Rect([0,25],[tw,th])
            targets.append(target)
            total_targets.append(target)
            directions.append([direction,direction1])
            for direction in directions:
                direction [0] = random.randint(0,1)
                direction [1] = random.randint(0,1)
            if len(dead_targets) >= 500:
                target_color = WHITE
                ts = 50
            elif len(dead_targets) > 480:
                target_color = PURPLE
                ts = 8.5
                user_color = PURPLE
                print("VICTORY!")
                us = 9
                bullet_life = 50
                if alreadyused == False:
                    userHP = 1000
                    alreadyused = True
            elif len(dead_targets) > 410:
                target_color = PURPLE
                ts = 8.5
                #userHP = user_HP + 50 
            elif len(dead_targets) > 360:
                target_color = INDIGO
                ts = 7.5
                user_color = INDIGO
                us = 8
                bullet_life = 30
                if alreadyused == True:
                    user_HP = 800
                    alreadyused == False
            elif len(dead_targets) > 300:
                target_color = INDIGO
                ts = 7.5
                #userHP = userHP + 45 
            elif len(dead_targets) > 250:
                target_color = BLUE
                ts = 6
                user_color = BLUE
                us = 7.5
                bullet_life = 12
                if alreadyused == False:
                    userHP = 600
                    alreadyused = True
            elif len(dead_targets) > 250:
                target_color = BLUE
                ts = 6
                #userHP = userHP + 40
            elif len(dead_targets) > 220:
                target_color = GREEN
                ts = 4.5
                user_color = GREEN
                us = 7
                if alreadyused == True:
                    userHP = 400
                    alreadyused = False
            elif len(dead_targets) > 180:
                target_color = GREEN
                ts = 4.5
                #userHP = userHP + 30
            elif len(dead_targets) > 130:
                target_color = YELLOW
                ts = 3.5
                user_color = YELLOW
                us = 6.5
                if alreadyused == False:
                    userHP = 200
                    alreadyused = True
            elif len(dead_targets) > 100:
                target_color = YELLOW
                ts = 3.5
                #userHP = userHP + 25
            elif len(dead_targets) > 50:
                target_color = ORANGE
                ts = 2.5
                user_color = ORANGE
                us = 5.5
                if alreadyused == True:
                    userHP = 100
                    alreadyused = False
            elif len(dead_targets) > 30:
                target_color = ORANGE
                ts = 2.5
                #userHP  = userHP + 20
            else:
                target_color = RED
                
                
        print(len(targets))
    else:
        
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
        if screen_mode == 'Instructions' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'title'
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
                if menu_screen_buttons[cur_menu_btn_id] == 'Instructions':
                    # if on resume button, go back to title screen
                    screen_mode = 'Instructions'
                elif menu_screen_buttons[cur_menu_btn_id] == 'Arena':
                    # if on random ('???') button, randomize background color
                    menu_screen_bg_color = [random.randint(0, 255),
                                            random.randint(0, 255),
                                            random.randint(0, 255)]
                    screen_mode ='Arena1'
        
                elif menu_screen_buttons[cur_menu_btn_id] == 'quit':
                    # if on quit button, quit the game
                    pygame.quit()
                    sys.exit()

        if screen_mode == 'Arena1' and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               print("pressed space")
               print(len(dead_targets))
               print(user.midright)
               pos = user.midright
               bullet_rect = pygame.Rect(pos[0], pos[1], bw, bh)
               variance_angle = 20
               
               angle = aim + 20
               
               bullet_y_vel = absolute_speed * math.sin(aim * (math.pi / 180))
               bullet_x_vel = -1 * (absolute_speed * math.cos(aim * (math.pi / 180)))
               bullet_life = bulletife
               bullets.append((bullet_rect, bullet_x_vel, bullet_y_vel, bullet_life))
               print(bullet_x_vel,bullet_y_vel)
            if event.key == pygame.K_w:
                aim -= 10
                if aim <= -20:
                    aim = -20
            if event.key == pygame.K_s:
                aim += 10
                if aim >= 20:
                    aim = 20
        
    

    frame = frame + 1
    clock.tick(FPS)
    pygame.display.update()

