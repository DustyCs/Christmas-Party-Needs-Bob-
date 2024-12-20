import pygame, time # type: ignore - VC can't detect
import _asyncio

from classes.player import *

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 30
run = True

# Player

player = Player() 
player.player_sprite_idle = pygame.image.load('design/Slime/Idle/Slime1_Idle_full.png').convert_alpha()
player.player_image = player.getImage(player.player_sprite_idle, player.frame_x, player.frame_y, 64, 64, 2, (0,0,0)) # not updating
player.player_rect = player.player_image.get_rect()

# Delta timer
# first time dealing with this
# try not to mess around with anything connected to this - too painful to find the bugs it would cause in the future ;;
previous_time = time.time()

while run:
    # Timer
    delta_time = time.time() - previous_time
    previous_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d], delta_time, FPS)

    window.fill((100, 100, 100))
    player.render(window)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



