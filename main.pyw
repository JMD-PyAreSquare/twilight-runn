#modules here
import random
import pygame
from pygame import *
import math

#initializing pygame
pygame.init()
pygame.mixer.init()

#constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0 ,0)
orange = (255, 165, 0)
yellow = (255, 255, 0)

WIDTH = 450
HEIGHT = 300
try:
    possible = True
    icon = pygame.image.load('assets/py.png')
except:
    possible = False

#vars
score = 0
player_x = 50
player_y = 200
x_change = 0
y_change = 0
gravity = 1
obstacles = [300, 450, 600]
obstacle_speed = 1.3
active = False
#window settings
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Runn!')
if possible:
    pygame.display.set_icon(icon)

fps = 60
font = pygame.font.Font('assets/impact.ttf', 32)
blocky = pygame.font.Font('assets/fff-forward.regular.ttf', 7)
timer = pygame.time.Clock()
background = pygame.image.load('assets/background.png')
overlap = pygame.image.load('assets/background.png')
my_file = open("database.local")
highscore = my_file.read()
my_file.close()
highscore = int(highscore)
running = True
pygame.mixer.music.load('assets/music.wav')
pygame.mixer.music.play(-1)
obs0w = 20
obs0h = 20
obs1w = 20
obs1h = 20
obs2w = 20
obs2h = 20
x0 = 0
x1 = 450
purple = (46, 20, 46)
screen.blit(background, (x0, 0))
screen.blit(overlap, (x1, 0))
while running:
    if x0 <= -450:
        x0 = 450
    if x1 <= -450:
        x1 = 450
    screen.fill(purple)
    if active:
        x0 -= obstacle_speed/4
        x1 -= obstacle_speed/4
    screen.blit(background, (x0, 0))
    screen.blit(overlap, (x1, 0))
    obstacle_speed += 0.001
    timer.tick(fps)
    score_text = font.render(f'SCORE: {score}'.format(), True, white)
    screen.blit(score_text, (40, 250))
    highscore_text = font.render(f'HIGH SCORE: {highscore}'.format(), True, white)
    screen.blit(highscore_text, (192, 250))
    credit = blocky.render('Program made by Jane Mat Dreiags'.format(), True, white)
    screen.blit(credit, (5, 5))
    floor = pygame.draw.rect(screen, purple, [0, 220, WIDTH, 10])
    player = pygame.draw.rect(screen, (142,64,142), [player_x, player_y, 20, 20])
    obstacle0 = pygame.draw.rect(screen, purple, [obstacles[0], 220-obs0h, obs0w, obs0h])
    obstacle1 = pygame.draw.rect(screen, purple, [obstacles[1], 220-obs1h, obs1w, obs1h])
    obstacle2 = pygame.draw.rect(screen, purple, [obstacles[2], 220-obs2h, obs2w, obs2h])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                score = 0
                obstacles = [300, 450, 600]
                obstacle_speed = 2
                player_x = 50
                active = True
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_LEFT:
                x_change = -1*obstacle_speed
            if event.key == pygame.K_RIGHT:
                x_change = 2

    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 600)
                if i == 0:
                    obs0w = random.randint(20, 30)
                    obs0h = random.randint(20, 40)
                if i == 1:
                    obs1w = random.randint(20, 40)
                    obs1h = random.randint(20, 30)
                if i == 2:
                    obs2w = random.randint(20, 60)
                    obs2h = random.randint(10, 30)
                score += 1
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                if score > highscore:
                    highscore = score
                    my_file = open("database.local", "w")
                    my_file.write(f"{highscore}\n")
                    my_file = open("database.local")
                    content = my_file.read()
                    my_file.close()
                
                active = False

    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0
    
    pygame.display.flip()
pygame.quit()
