import pygame, time, os # type: ignore - VC can't detect
import _asyncio
from pytmx.util_pygame import load_pygame

from classes.player import *
from classes.background import *
from utils.visual_test import LineTest
from classes.groups import AllSprites

pygame.init()

window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 30
run = True


# Sprites

all_sprites = AllSprites()
collision_sprites = pygame.sprite.Group()

# Player

player = Player((2160, 4600), all_sprites, collision_sprites) 

# Load Map


def setup():
    map = load_pygame(os.path.join('design', 'tiled', 'World Map.tmx'))
    scale = 2

    tile_size = 32 * scale

    for x, y, image in map.get_layer_by_name('Ground').tiles():
        BackgroundSprite((x * tile_size , y * tile_size), image, all_sprites, scale)

    # for x, y, image in map.get_layer_by_name('Decorations').tiles():
    #     BackgroundSprite((x * tile_size , y * tile_size), image, all_sprites, scale)

    for obj in map.get_layer_by_name('Collisions'):
        CollisionSprite((obj.x * scale, obj.y * scale), obj.image, (all_sprites, collision_sprites), scale)

setup()

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


    window.fill((255, 255, 255))
    all_sprites.draw(player.rect.center)
    pygame.draw.rect(window, (0, 255, 255), player.hitbox_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()