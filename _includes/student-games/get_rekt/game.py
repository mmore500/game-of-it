import sys
import random
import pygame
import time

pygame.init()

#OBJECTIVES
#ENEMIES (Spawn more enemies + spawn powerups on dead enemies)

#AMMO (AMMO IF POSSIBLE)
#MAYBE DIFFERENT WEAPONS

# ---Standard Variables---
fps = 60
scrn_w = 1200 #Width
scrn_h = 800 #Height
btn_padding = 10
btn_margin = 10
got_time = 0
got_speed = False
got_freeze = False
# ---Screen & Clock---
screen = pygame.display.set_mode([scrn_w, scrn_h])
clock = pygame.time.Clock()

# ---Music---
pygame.mixer.music.load('lofi.ogg')
pygame.mixer.music.play(-1)


# ---Colors---
BLACK = [0, 0, 5]
GREY = [175, 175, 175]
WHITE = [255, 255, 255]
RED = [220,60,50]
DARK_RED = [125, 0, 0]
GREEN = [80,200,25]
DARK_GREEN = [5, 150, 10]
BLUE = [25,90,170]
LIGHT_BLUE = [120,195,225]
ORANGE = [255,120,0]

# ---Different Screens---

screen_mode = "title"

###########
# ---Title Screen---
title_scrn_color = GREY
title_font = pygame.font.SysFont('impact', 100)
title_button_font = pygame.font.SysFont('impact',30)
#    ---- Title Text & Buttons ----
#Title Text
title_surface = title_font.render("GET_REKT()", True,BLUE)#Color needed
title_rect = title_surface.get_rect()
title_rect.x = (scrn_w / 2) - (title_rect.width / 2)
title_rect.y = (scrn_h / 2) - (title_rect.height)

# Title Button
title_btn_txt_surface = title_button_font.render("Start Game", True,BLACK)#Color needed
# Title Button Background
title_btn_bg_rect = title_btn_txt_surface.get_rect()
title_btn_bg_rect.width += 2 * btn_margin
title_btn_bg_rect.height += 2 * btn_margin
title_btn_bg_rect.x = title_rect.midbottom[0] - (title_btn_bg_rect.width / 2)
title_btn_bg_rect.y = title_rect.midbottom[1]
# Title Button Text
title_btn_txt_rect = title_btn_txt_surface.get_rect()
title_btn_txt_rect.x = title_btn_bg_rect.x + btn_margin
title_btn_txt_rect.y = title_btn_bg_rect.y + btn_margin


###########
# ---Power Ups---

def generate_powerup(name=''):
    rx = random.randint(50,400)
    rxt = random.randint(800,1150)

    ry = random.randint(50,300)
    ryt = random.randint(500,750)
    PU_start_x = random.choice([rx,rxt])
    PU_start_y = random.choice([ry,ryt])

    health = pygame.Rect([PU_start_x,PU_start_y],[15,15])
    speed = pygame.Rect([PU_start_x,PU_start_y],[15,15])
    freeze = pygame.Rect([PU_start_x,PU_start_y],[15,15])

    powerups = [
        {'name': 'health', 'rect': health},
        {'name': 'speed', 'rect': speed},
        {'name': 'freeze', 'rect': freeze}]

    return next(i for i in powerups if i['name'] == name) if name else random.choice(powerups)


current_powerups = [generate_powerup()]


###########
# ---Weapons---
weapon_start_x = random.randint(0,1200)
weapon_start_y = random.randint(0,800)

revolver = pygame.Rect([weapon_start_x,weapon_start_y],[15,15])
tommy = pygame.Rect([weapon_start_x,weapon_start_y],[15,15])
shotgun = pygame.Rect([weapon_start_x,weapon_start_y],[15,15])


weapons = [revolver, tommy, shotgun]
weapon_mode = 0
ammunition = 0



###########
# ---Enemies---
enemies_color = RED
enemies = []
amount_enemies = 3
enemy_width = 22
enemy_height = 22
enemy_speed = 2

safe_space = pygame.Rect(200,200,800,400)

def get_enemy_rect():
    while True:
        enemy_width = 22
        enemy_height = 22
        enemy_x = random.randint(0,900)
        enemy_y = random.randint(0,900)

        # print(enemy_x,", ", enemy_y)

        enemy_rect = pygame.Rect([enemy_x,enemy_y],[enemy_width,enemy_height])
        if not enemy_rect.colliderect(safe_space):
            return enemy_rect

for i in range(amount_enemies):
    enemies.append(get_enemy_rect())


###########
# ---Lives/Player---
char_start_x = title_rect.x - 23
char_start_y = title_rect.y + 80
char_width = 22
char_height = 22
char_speed = 3
cur_char_x_vel = 0
cur_char_y_vel = 0
character = pygame.Rect([char_start_x, char_start_y], [char_width, char_height])

direction = "right"

lives = 3
lives_font = pygame.font.SysFont('impact', 30)

###########
# ---Projectiles---
projectiles = []
projectile_width = 10
projectile_height = 5

projectile_color = BLACK
projectile_speed = 5
projectile_direction = []
#Projectile Rectangle is by the pygame.K_Space event


###########
# ---Death Screen---
death_scrn_color = BLACK
death_font = pygame.font.SysFont('impact', 100)
death_button_font = pygame.font.SysFont('impact',30)

death_surface = death_font.render("U.GOT_REKT()", True,DARK_RED)#Color needed
death_rect = title_surface.get_rect()
death_rect.x = (scrn_w / 2) - (death_rect.width / 2)
death_rect.y = (scrn_h / 2) - (death_rect.height)

death_btn_txt_surface = death_button_font.render("Play Again?", True,BLACK)#Color needed
# Title Button Background
death_btn_bg_rect = death_btn_txt_surface.get_rect()
death_btn_bg_rect.width += 2 * btn_margin
death_btn_bg_rect.height += 2 * btn_margin
death_btn_bg_rect.x = death_rect.midbottom[0] - (death_btn_bg_rect.width / 2)
death_btn_bg_rect.y = death_rect.midbottom[1]
# death Button Text
death_btn_txt_rect = death_btn_txt_surface.get_rect()
death_btn_txt_rect.x = death_btn_bg_rect.x + btn_margin
death_btn_txt_rect.y = death_btn_bg_rect.y + btn_margin

while True:

    if screen_mode == "title":
        screen.fill(title_scrn_color)
        screen.blit(title_surface, title_rect)
        pygame.draw.rect(screen,RED,title_btn_bg_rect)
        screen.blit(title_btn_txt_surface, title_btn_txt_rect)


        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cur_char_y_vel = -1*char_speed
            direction = "up"
        elif pressed_keys[pygame.K_DOWN]:
            cur_char_y_vel = char_speed
            direction = "down"
        else:
            cur_char_y_vel = 0
        if pressed_keys[pygame.K_RIGHT]:
            cur_char_x_vel = char_speed
            direction = "right"
        elif pressed_keys[pygame.K_LEFT]:
            cur_char_x_vel = -1*char_speed
            direction = "left"
        else:
            cur_char_x_vel = 0

        character.left += cur_char_x_vel
        if character.left <= 0:
            character.left = 0
        elif character.right >= scrn_w:
            character.right = scrn_w
        character.top += cur_char_y_vel
        if character.top <= 0:
            character.top = 0
        elif character.bottom >= scrn_h:
            character.bottom = scrn_h
        pygame.draw.rect(screen, DARK_GREEN, character)


        for powerup in current_powerups:
            rect = powerup['rect']
            name = powerup['name']
            pygame.draw.rect(screen, GREEN, rect)



        for i in range (0, len(projectiles)):

            pygame.draw.rect(screen, BLACK, projectiles[i])

        for i, projectile in enumerate(projectiles):
            if projectile_direction[i] == "up":
                projectile.top -= projectile_speed
            elif projectile_direction[i] == "right":
                projectile.right += projectile_speed
            elif projectile_direction[i] == "down":
                projectile.top += projectile_speed
            elif projectile_direction[i] == "left":
                projectile.left -= projectile_speed


    elif screen_mode == "play":
        screen.fill(WHITE)


        if got_freeze == True:
            cur_time = time.time()
            elapsed_time = int(cur_time - got_time)
            text = lives_font.render("Freeze: "+ str(2 - elapsed_time), True, BLACK)
            screen.blit(text, [50, 150])
            if elapsed_time > 2:
                got_freeze = False
                enemy_speed = 2


        if got_speed == True:
            cur_time = time.time()
            elapsed_time = int(cur_time - got_time)
            text = lives_font.render("Speed Boost: "+ str(5 - elapsed_time), True, BLACK)
            screen.blit(text, [50, 100])
            if elapsed_time > 5:
                got_speed = False
                char_speed -= 2



        current_time = time.time()
        elapsed = int(current_time - start_time)
        text = lives_font.render(str(elapsed), True, BLACK)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cur_char_y_vel = -1*char_speed
            direction = "up"
        elif pressed_keys[pygame.K_DOWN]:
            cur_char_y_vel = char_speed
            direction = "down"
        else:
            cur_char_y_vel = 0
        if pressed_keys[pygame.K_RIGHT]:
            cur_char_x_vel = char_speed
            direction = "right"
        elif pressed_keys[pygame.K_LEFT]:
            cur_char_x_vel = -1*char_speed
            direction = "left"
        else:
            cur_char_x_vel = 0

        character.left += cur_char_x_vel
        if character.left <= 0:
            character.left = 0
        elif character.right >= scrn_w:
            character.right = scrn_w
        character.top += cur_char_y_vel
        if character.top <= 0:
            character.top = 0
        elif character.bottom >= scrn_h:
            character.bottom = scrn_h
        pygame.draw.rect(screen, DARK_GREEN, character)

        for powerup in current_powerups:
            rect = powerup['rect']
            name = powerup['name']
            pygame.draw.rect(screen, GREEN, rect)
            if character.colliderect(rect):
                if name == 'health':

                    print('got health')
                    lives = lives + 1

                elif name == 'speed':

                    print('got speed')
                    char_speed += 2
                    got_time = time.time()
                    got_speed = True

                elif name == 'freeze':
                    print('frozen')
                    enemy_speed -= 2
                    got_time = time.time()
                    got_freeze = True
                else:
                    print('name is', name)
                current_powerups.remove(powerup)
                #current_powerups.append(generate_powerup())
            else:
                pass

        for i in range (0, len(projectiles)):

            pygame.draw.rect(screen, [197,212,208], projectiles[i])

        for i, projectile in enumerate(projectiles):
            if projectile_direction[i] == "up":
                projectile.top -= projectile_speed
            elif projectile_direction[i] == "right":
                projectile.right += projectile_speed
            elif projectile_direction[i] == "down":
                projectile.top += projectile_speed
            elif projectile_direction[i] == "left":
                projectile.left -= projectile_speed

        for enemy in enemies:
            pygame.draw.rect(screen, ORANGE , enemy)
        for enemy in enemies:
            if character.x > enemy.left:
                enemy.left += enemy_speed
            if character.x < enemy.left:
                enemy.left -= enemy_speed
            if character.y > enemy.top:
                enemy.top += enemy_speed
            if character.y < enemy.top:
                enemy.top -= enemy_speed

        if len(enemies) == 0 and screen_mode == "play":
            amount_enemies += 2
            for i in range(amount_enemies):
                enemies.append(get_enemy_rect())

        enemies_kill = []
        for i in reversed(range(len(enemies))):
            for project in range(len(projectiles)):
                if projectiles[project].colliderect(enemies[i]):
                    enemies_kill.append(i)
                    print("Enemy Died")
                    if random.random() <= 0.15:
                        current_powerups.append(generate_powerup())
                else:
                    pass


        for i in reversed(range(len(enemies))):
            if character.colliderect(enemies[i]):
                enemies_kill.append(i)
                lives -= 1
            else:
                pass

        a = []
        for i in range(0, len(enemies)):
            if i not in enemies_kill:
                a.append(enemies[i])
        enemies = a

        #for i in reversed(range(len(enemies_kill))):

         #   del enemies[i]



        lives_surface = lives_font.render('LIVES: ' + str(lives), True, BLACK)
        lives_rect = lives_surface.get_rect()
        lives_rect.x = scrn_w - lives_rect.width - 50
        lives_rect.y = 50


        screen.blit(lives_surface, lives_rect)
        screen.blit(text, (50, 50))
        if lives <= 0:
            screen_mode = "death"
    elif screen_mode == "death":
        score_txt_font = pygame.font.SysFont('impact',30)
        score_txt_surface = score_txt_font.render("Wave Enemies: "+str(amount_enemies), True,WHITE)
        score_txt_rect = score_txt_surface.get_rect()
        score_txt_rect.x = 50
        score_txt_rect.y = 50

        screen.fill(BLACK)
        screen.blit(death_surface, death_rect)
        pygame.draw.rect(screen,DARK_RED,death_btn_bg_rect)
        screen.blit(death_btn_txt_surface, death_btn_txt_rect)
        screen.blit(score_txt_surface,score_txt_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet
                print("pressed space")
                print(direction)
                pos = [0,0]
                if direction == "up":
                    projectile_direction.append("up")
                    pos = character.midtop
                    h = projectile_width
                    w = projectile_height
                elif direction == "down":
                    projectile_direction.append("down")
                    pos = character.midbottom
                    h = projectile_width
                    w = projectile_height
                elif direction == "right":
                    projectile_direction.append("right")
                    pos = character.midright
                    h = projectile_height
                    w = projectile_width
                elif direction == "left":
                    projectile_direction.append("left")
                    pos = character.midleft
                    h = projectile_height
                    w = projectile_width
                projectile = pygame.Rect([pos[0], pos[1]], [w, h])
                projectiles.append(projectile)
        if screen_mode == 'title' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if title_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'play'
                start_time = time.time()
        if screen_mode == 'death' and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if death_btn_bg_rect.collidepoint(mouse_pos):
                screen_mode = 'play'
                lives = 3
                start_time = time.time()
                amount_enemies = 3
                enemies = []
                for i in range(amount_enemies):
                    enemies.append(get_enemy_rect())

    clock.tick(fps)
    pygame.display.flip()
