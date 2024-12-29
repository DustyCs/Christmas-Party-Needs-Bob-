import pygame, time # type: ignore - VC can't detect
import _asyncio
from pytmx.util_pygame import load_pygame

from classes.player import *
from classes.background import *
from utils.visual_test import LineTest

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 30
run = True

# Player

player = Player() 
player.player_sprite_idle = pygame.image.load('design/Slime/Idle/Slime1_Idle_full.png').convert_alpha()
player.player_sprite_run = pygame.image.load('design/Slime/Run/Slime1_Run_full.png').convert_alpha()
player.player_image = player.getImage(player.player_sprite_idle, player.frame_x, player.frame_y, 64, 64, 2, (0,0,0))
player.player_rect = player.player_image.get_rect()
player.player_rect.x, player.player_rect.y = 600, 235

# Background
stage1_img = pygame.image.load('design/background/Background1.png').convert_alpha()
background = Background(stage1_img, 300, 75, 2)
 
bg_house = [(240, 180), 140, 400] # size, x, y
fenced_area = [(50, 50), 0, 0]
background.objects = [bg_house, fenced_area]

# DT try not to mess around with anything connected to this - too painful to find the bugs it would cause in the future ;;
previous_time = time.time()

while run:
    # DTimer
    delta_time = time.time() - previous_time
    previous_time = time.time() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d], delta_time, FPS)

    window.fill((100, 100, 100))
    background.render(window, player.player_rect) # 
    player.render(window) 

    # print(player.player_rect.x)

    # test collision

    # print(pygame.Rect.colliderect(player.player_rect, background.objects_rect[0]))

    if (pygame.Rect.colliderect(player.player_rect, background.objects_rect[0])):
        player.collision = True
    else:
        player.collision = False
    # print(player.player_rect.x, player.player_rect.y)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()