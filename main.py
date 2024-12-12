import pygame # type: ignore - VC can't detect
from classes.player import *

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 20
run = True

# Player

player = Player() 
player.player_sprite_idle = pygame.image.load('design/Slime/Idle/Slime1_Idle_full.png').convert_alpha()


player.player_image = pygame.image.load('design/Bob.png').convert_alpha()
player.player_rect = player.player_image.get_rect()
player.side_imgs = [pygame.image.load('design/sides/side' + str(x) + '.png') for x in range(4)] # list comprehension
player.up_imgs = [pygame.image.load('design/up/up' + str(x) + '.png') for x in range(6)]
player.down_imgs = [pygame.image.load('design/down/down' + str(x) + '.png') for x in range(6)]


def getImage(sheet, frame_x, frame_y, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    
    image.blit(sheet, (0, 0), ((frame_x * width), (64 * frame_y), width, (height * frame_x))) # area x = 0, y = 0, width, height
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

BLACK = (0,0,0)
frame_0 = getImage(player.player_sprite_idle, 0, 0, 64, 64, 2, BLACK)
frame_x = 1
frame_y = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d])
   

    window.fill((100, 100, 100))
    # player.render(window)
    
    window.blit(getImage(player.player_sprite_idle, frame_x, frame_y, 64, 64, 3, BLACK), (player.player_rect))
    frame_x += 1
    if frame_x == 6:
        if frame_y <= 3:
            frame_y += 1
            if frame_y == 4:
                frame_y = 0
        
    if frame_x >= 6:
        frame_x = 0
        
    print(frame_x, frame_y)
    # window.blit(player.player_sprite_idle, (0, 0))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



