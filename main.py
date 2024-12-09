import pygame # type: ignore - VC can't detect
from classes.player import *

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60
run = True

# Player

player_img = pygame.image.load('design/Bob.png').convert_alpha()
player_rect = player_img.get_rect()
player = Player(player_img, player_rect)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player.testPrint()
    player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d])
    player.render(window)



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



