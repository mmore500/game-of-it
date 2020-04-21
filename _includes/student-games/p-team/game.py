'''
Bullet shooter game
'''

import sys
import random
import pygame
import math

pygame.init()

# let's try to avoid magic numbers for this
screen_width = 900
screen_height = 900
wall_size = 25
FPS = 60

RED = [255, 0, 0]
LIGHT_GREY = [230, 230, 230]
BLACK = [0, 0, 0]
BLUE = [0,0,230]
GREEN = [0, 255, 0]
ARMY_GREEN = [72, 107, 7]
BLACK = [0,0,0]
BULLET_SPEED = 20

font = pygame.font.SysFont('swmono', 20)


health_color = [255,255,255]
health_bg = [0,0,0]

health_img = pygame.image.load("health_bar.png")
health_img = pygame.transform.scale(health_img, (150,30))

score_board_img = pygame.image.load("health_bar.png")
score_board_img = pygame.transform.scale(score_board_img, (150,30))

health_x = 25
health_y = 25

health_cords = [health_x, health_y]
'''
score_x1 = 700
score_y1 = 25
score_cords1 = [score_x1, score_y1]
'''
score_x = 700
score_y = 30
score_cords = [score_x, score_y]

score_color = [0,0,0]
score_bg = [255,255,255]
score_surface = font.render('Score:', True, score_color, score_bg)


leftwall = pygame.Rect(0, 0, wall_size, screen_height)
rightwall = pygame.Rect(screen_width - wall_size, 0, wall_size, screen_height)
topwall = pygame.Rect(0, 0, screen_width, wall_size)
bottomwall = pygame.Rect(0, screen_height - wall_size, screen_width, wall_size)

#Data that stores types and locations of every wall, 0 = full wall, 1 = wall w/ door, 2 = no wall.

vertical_walltype = {0: [wall_size, screen_height / 3], 1: [wall_size, (screen_height / 3) - (screen_height/12)], 2: [0, 0]} 
horizontal_walltype = {0: [screen_width / 3, wall_size], 1: [(screen_width / 3) - (screen_width/12), wall_size], 2: [0, 0]}
verticalwall_locations = [[(screen_width/3) - wall_size/2, 0], [(2*screen_width/3) - wall_size/2, 0], [(screen_width/3) - wall_size/2, (screen_height/3) - wall_size/2], [(2*screen_width/3) - wall_size/2, (screen_height/3) - wall_size/2], [(screen_width/3) - wall_size/2, (2*screen_height/3) - wall_size/2], [(2*screen_width/3) - wall_size/2, (2*screen_height/3) - wall_size/2]]
horizontalwall_locations = [[0,(screen_height/3) - wall_size/2],[0,(2*screen_height/3) - wall_size/2],[(screen_width/3) - wall_size/2, (screen_height/3) - wall_size/2], [(screen_width/3) - wall_size/2,(2*screen_height/3) - wall_size/2],[(2*screen_width/3) - wall_size/2, (screen_height/3) - wall_size/2],[(2*screen_width/3) - wall_size/2,(2*screen_height/3) - wall_size/2]]

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Take Aim")

clock = pygame.time.Clock()

char_start_x = 450
char_start_y = 450
char_x_val = 450    #this is the x cordinate value
char_y_val = 450    #this is the y cordinate value
char_width = 30
char_height = 30
char_speed = 5    # How fast does character move?
cur_char_x_vel = 0  # What's the character's current x speed?
cur_char_y_vel = 0  # What's the character's current y speed?

bullets = [] # Here's where we'll track all of the bullets on the screen
gun_length = 25

'''
bullet_velocity_x = 10 # How fast should bullets move?
bullet_width = 7.5
bullet_height = 5
'''

character = pygame.Rect([char_x_val, char_y_val], [char_width, char_height])

target_img = pygame.image.load("target_transparent.png")
floor_img = pygame.image.load("Floor.png")
target_img_box = target_img.get_rect()
floor_img_box = floor_img.get_rect()

health = 500
max_health = 500
print(health)
score = 0

next_room=0

safe_space = pygame.Rect(250,250,450,450)

def generate_level():
    verticalwall_typelist = [0, 0, 0, 0, 0, 0]
    horizontalwall_typelist = [0, 0, 0, 0, 0, 0]
    for wall in range(6):
        verticalwall_typelist[wall] = random.randrange(3)
    for wall in range(6):
        horizontalwall_typelist[wall] = random.randrange(3)
    return verticalwall_typelist, horizontalwall_typelist

def draw_level():
    vwall = []
    hwall = []
    for w_type, location in zip(verticalwall_typelist, verticalwall_locations):
        temporary_wall = (location + vertical_walltype[w_type])
        wallrect = pygame.draw.rect(screen, [0, 0, 0], temporary_wall)
        vwall.append(wallrect)
    for w_type, location in zip(horizontalwall_typelist, horizontalwall_locations):
        temporary_wall = (location + horizontal_walltype[w_type])
        wallrect = pygame.draw.rect(screen, [0, 0, 0], temporary_wall)
        hwall.append(wallrect)
    return vwall, hwall

#Retry loop / floor loop

verticalwall_typelist, horizontalwall_typelist = generate_level()

most_recent_dir = ''

def get_enemy_rect():
    while True:
        enemy_width = 25
        enemy_height = 25
        enemy_x_val = random.randint(0,900)
        enemy_y_val = random.randint(0,900)
        
        # print(enemy_x_val,", ", enemy_y_val)

        enemy_rect = pygame.Rect([enemy_x_val,enemy_y_val],[enemy_width,enemy_height])
        if not enemy_rect.colliderect(safe_space):
            return enemy_rect

enemies = []
amount_enemies = 3
place_holder_enemies = 3

for i in range(amount_enemies):
    enemies.append(get_enemy_rect())


dead = False

while True:
    screen.fill(LIGHT_GREY)
    screen.blit(floor_img, floor_img_box)
    if not dead:
        screen.blit(health_img, health_cords)
        health_rect=health_img.get_rect()
        health_rect.x = health_cords[0] + 5
        health_rect.y = health_cords[1] + 5
        health_rect.width -= 10
        health_rect.height -= 10
        health_rect.width *= health/max_health
          
        pygame.draw.rect(screen, RED, health_rect)
        
        score_txt_font = pygame.font.SysFont('impact',30)
        score_txt_surface = score_txt_font.render("Score: "+str(score), True,BLACK)
        score_txt_rect = score_txt_surface.get_rect()
        score_txt_rect.x = 750
        score_txt_rect.y = 25
            

        screen.blit(score_txt_surface,score_txt_rect)
        
        #screen.blit(score_board_img, score_cords1)
        #screen_rect=score_img.get_rect()

        collide = False
        pygame.draw.rect(screen, [0, 0, 0], topwall)
        pygame.draw.rect(screen, [0, 0, 0], bottomwall)
        pygame.draw.rect(screen, [0, 0, 0], leftwall)
        pygame.draw.rect(screen, [0, 0, 0], rightwall)
        
        v_walls, h_walls = draw_level()
        all_walls = v_walls + h_walls + [topwall , bottomwall , leftwall , rightwall]
        vwalls = v_walls + [leftwall, rightwall]
        hwalls = h_walls + [topwall, bottomwall]
        
        pygame.mouse.set_visible(False)
        mouse_pos = pygame.mouse.get_pos()
        line_vec = [mouse_pos[0] - character.centerx, mouse_pos[1] - character.centery]
        vec_len = math.hypot(line_vec[0], line_vec[1])
        vec = [(line_vec[0] / vec_len) * gun_length, (line_vec[1] / vec_len) * gun_length]
        char_center = [character.centerx, character.centery]
        pygame.draw.line(screen, BLACK, char_center, [char_center[0] + vec[0], char_center[1] + vec[1]], 5)
    #    character.left += cur_char_x_vel
    #    character.top += cur_char_y_vel
        
        
        target_img_box.centerx = mouse_pos[0]
        target_img_box.centery = mouse_pos[1]
        screen.blit(target_img, target_img_box)
        #screen.blit(floor_img, floor_img_box)
        
    #    pygame.draw.rect(screen, GREEN, safe_space)
        # Determine character movement
        # Is the player pressing a key?
        # - Is player moving vertically?
        
        pressed_keys = pygame.key.get_pressed()
        
        bounce_back_distance = 10
        
        if pressed_keys[pygame.K_w]:
            #print("up arrow")
            cur_char_y_vel = -1*char_speed
            char_y_val -= 5
            char_clock = pygame.time.Clock()
            char_start_y -= 5
        elif pressed_keys[pygame.K_s]:
            #print("down arrow")
            cur_char_y_vel = char_speed
            char_y_val += 5
            char_start_y += 5
        else:
            cur_char_y_vel = 0
        # - Is player moving horizontally?
        if pressed_keys[pygame.K_d]:
            #print("down arrow")
            cur_char_x_vel = char_speed
            char_x_val += 5
            char_start_x += 5
        elif pressed_keys[pygame.K_a]:
            #print("down arrow")
            cur_char_x_vel = -1*char_speed
            char_x_val -= 5
            char_start_x -= 5
        else:
            cur_char_x_vel = 0
            
        for wall in vwalls:
            collide = character.colliderect(wall)
            if collide:
                #collide_x = abs(character.centerx - wall.centerx) <= (character.width/2 + wall.width/2)
                if (character.centerx - wall.centerx) < 0:
                    character.right = wall.left - 1
                else:
                    character.left = wall.right - 1
        for wall in hwalls:
            collide = character.colliderect(wall)
            if collide:
                #collide_y = abs(character.centery - wall.centery) <= (character.height/2 + wall.height/2)
                if (character.centery - wall.centery) > 0:
                    character.top = wall.bottom - 1
                else:
                    character.bottom = wall.top - 1
            
            
        
        for bullet in bullets:
            # Draw the bullet
            bullet["current_loc"][0] += (BULLET_SPEED * bullet["direction"][0])
            bullet["current_loc"][1] += (BULLET_SPEED * bullet["direction"][1])
            cur_loc = bullet["current_loc"]
            pygame.draw.circle(screen, BLACK, [int(cur_loc[0]), int(cur_loc[1])], 3)

        # Draw the character!
        character.left += cur_char_x_vel
        character.top += cur_char_y_vel
        pygame.draw.rect(screen, ARMY_GREEN, character)

        # Draw the enemies!
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        # Draw the bullets!
        # Challenge: Every time you click, fire bullets from your mouse
        # Challenge: Have bullets that collide with enemies remove that enemy from the screen
        # Challenge: clean up off-screen bullets
        # Challange: spawn new enemies
        
        on_screen_bullets = []
        for bullet in bullets:
            alive_enemies = []
            for enemy in enemies:
                x_y = bullet["current_loc"]
                bullet_rect = pygame.Rect(x_y, [3, 3])
                if bullet_rect.colliderect(enemy):
                    clock = pygame.time.Clock()
                    amount_enemies -= 1
                    score = score + 1
                    if amount_enemies == 0:
                        place_holder_enemies += 1
                        amount_enemies = place_holder_enemies
                        for i in range(amount_enemies):
                            enemies.append(get_enemy_rect())
                        
                        verticalwall_typelist, horizontalwall_typelist = generate_level()
                    continue
                alive_enemies.append(enemy)

            enemies = alive_enemies

            if bullet_rect.left <= screen_width:
                on_screen_bullets.append(bullet)
        bullets = on_screen_bullets
        
        for enemy in enemies:
            if character.colliderect(enemy):
                health = health - 1
                print("Health: ", health)
        
        if(health <= 0):
            print("YOU DIED SUCKER!!!")
            print("Score: ",score)
            dead = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Keydown event!
                '''
                if event.key == pygame.K_SPACE:
                    # Fire a bullet
                    print("pressed space")
                    print(character.midright)
                    pos = character.midright
                    bullet = pygame.Rect(pos[0], pos[1], bullet_width, bullet_height)
                    bullets.append(bullet)
                '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                #pygame.mixer.music.load("gunshot.ogg")
                #pygame.mixer.music.play(1, 0.0)
                line_vec = [mouse_pos[0] - character.centerx, mouse_pos[1] - character.centery]
                vec_len = math.hypot(line_vec[0], line_vec[1])
                unit_vec = [line_vec[0] / vec_len, line_vec[1] / vec_len]
                #print("====")
                #print("Line vec: " + str(line_vec) + "; Unit vec: " + str(unit_vec))
                bullets.append({"current_loc": [character.centerx, character.centery], "direction": unit_vec})
            
        for enemy in enemies:
                
            if character.centerx > enemy.centerx:
                enemy.left += 2
            
            if character.centerx < enemy.centerx:
                enemy.left -= 2 
            
            if character.centery > enemy.centery:
                enemy.top += 2
            
            if character.centery < enemy.centery:
                enemy.top -= 2

    else:
        pygame.mouse.set_visible(True)
        font = pygame.font.SysFont('impact', 100)
        game_over = font.render('You were slain!', True, [100, 0, 0])
        screen.blit(game_over, [100, 300])
        small_font = pygame.font.SysFont('impact', 60)
        #score_text = 'Your score:', score
        score_display = small_font.render('Your score: ' + str(score), True, [100, 0, 0])
        screen.blit(score_display, [100, 500])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
    pygame.display.update()
    clock.tick(FPS)
