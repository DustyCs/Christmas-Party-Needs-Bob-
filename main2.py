import pygame, time, os # type: ignore - VC can't detect
from pytmx.util_pygame import load_pygame

from classes.groups import AllSprites
from classes.player import *
from classes.background import *
from utils.visual_test import LineTest


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Bob's Adventure")
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 30

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        
        

    def setup(self):
        map = load_pygame(os.path.join('design', 'tiled', 'World Map.tmx'))
        scale = 2
        tile_size = 32 * scale


        for x, y, image in map.get_layer_by_name('Ground').tiles():
            BackgroundSprite((x * tile_size , y * tile_size), image, self.all_sprites, scale)
        
        # for obj in map.get_layer_by_name('Objects'):
        #     CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Tents'):
            CollisionSprite((obj.x * scale, obj.y * scale), obj.image, (self.all_sprites, self.collision_sprites), scale)
        
        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x * scale, obj.y * scale), obj.image, (self.all_sprites, self.collision_sprites), scale, obj.name)
            
        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x * scale, obj.y * scale), self.all_sprites, self.collision_sprites)
                # print(obj.x, obj.y)

    def run(self):
        previous_time = time.time()

        while self.running:
            # DTimer

            delta_time = time.time() - previous_time
            previous_time = time.time() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.movement(keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d], delta_time, self.FPS)

            # game progression
            
            # for sprites in self.collision_sprites:
            #     if sprites.name == "Gate 2":
            #         sprites.kill()

            # draw
            self.display_surface.fill((255, 255, 255))

            self.all_sprites.draw(self.player.rect.center)
            # print(self.player.hitbox_rect)
            pygame.display.flip()
            self.clock.tick(self.FPS)


        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()