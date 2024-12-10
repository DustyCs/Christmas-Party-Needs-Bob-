import pygame # type: ignore - VC can't detect
from classes.player import *

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60
run = True

# Player

player = Player() 
player.player_image = pygame.image.load('design/Bob.png').convert_alpha()
player.player_rect = player.player_image.get_rect()
player.side_imgs = [pygame.image.load('design/sides/side' + str(x) + '.png') for x in range(4)] # list comprehension
player.up_imgs = [pygame.image.load('design/up/up' + str(x) + '.png') for x in range(6)]
player.down_imgs = [pygame.image.load('design/down/down' + str(x) + '.png') for x in range(6)]

count = 0 # to update the frame bring the counter out

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # player.testPrint()
    

    player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d])
    window.fill((0, 0, 0))
    window.blit(player.side_imgs[count], player.player_rect) # frame isn't updated since it inside the loop
    count += 1
    print(count)
    if count >= 3:
        count = 0
    
    # player.render(window)

    # print(player.side_imgs)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



