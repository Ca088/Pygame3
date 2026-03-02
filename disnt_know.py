import random
import math
import pygame

scrWidth=800
scrHeight=700
player_start_x=350
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27

pygame.init()
screen=pygame.display.set_mode((scrWidth, scrHeight))
pygame.display.set_caption("Space Invaders")
bg=pygame.image.load("background.png")
screen.blit(bg, (0,0))



playerImg=pygame.image.load("player.png")
player_x=player_start_x
player_y=player_start_y







enemyImg=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemies=7

for _ in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, scrWidth - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)


bullet_img=pygame.image.load("bullet.png")
bullet_x=0
bullet_y=player_y
bullet_state="ready"


score=0
font=pygame.font.Font("freesansbold.ttf", 32)
text_x=10
text_y=10


over_font=pygame.font.Font("freesansbold.ttf", 64)


def show_score(x,y):
    score_show=font.render("Score:"+str(score),True,"white")
    screen.blit(score_show,(x,y))
    
def lose(x,y):
    show_lose=font.render("You lose!",True,"white")
    screen.blit(show_lose,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x+16,y+10))

def isColliderect(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=math.sqrt(math.pow(enemy_x-bullet_x,2)+math.pow(enemy_y-bullet_y,2))
    if distance<collision_distance:
        return True
    else:
        return False
    

