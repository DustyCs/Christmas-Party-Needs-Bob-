import pygame # type: ignore - VC can't detect
from classes import player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60
run = True

player = player.Player()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.testPrint()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()



