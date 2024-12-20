import pygame # type: ignore - VC can't detect

from classes.player import *

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60
run = True

# Player

player = Player() 
player.player_sprite_idle = pygame.image.load('design/Slime/Idle/Slime1_Idle_full.png').convert_alpha()
player.player_image = player.getImage(player.player_sprite_idle, player.frame_x, player.frame_y, 64, 64, 2, (0,0,0)) # not updating
player.player_rect = player.player_image.get_rect()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d])

    window.fill((100, 100, 100))
    player.render(window)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



