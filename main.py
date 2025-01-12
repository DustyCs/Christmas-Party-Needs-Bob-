import pygame, time, os # type: ignore - VC can't detect
from pytmx.util_pygame import load_pygame # type: ignore
import cv2 # type: ignore

from classes.groups import AllSprites
from classes.player import *
from classes.background import *
from classes.mainmenu import MainMenu, MenuButton
from classes.inventory_system import InventoryBar, Item

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Bob's Adventure")
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 30
        self.main_menu = False
        self.game_intro = cv2.VideoCapture('design/Main Menu/game_intro.mp4')
        self.introFPS = self.game_intro.get(cv2.CAP_PROP_FPS)
        self.success, self.video_image = self.game_intro.read()

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.inventory_bar = InventoryBar((640, 40))

        self.menu_sprites = pygame.sprite.Group()

        self.mainMenu = MainMenu(self.menu_sprites)

        self.setup()

    def setup(self):
        map = load_pygame(os.path.join('design', 'tiled', 'World Map.tmx'))
        scale = 2
        tile_size = 32 * scale

        for x, y, image in map.get_layer_by_name('Ground').tiles():
            BackgroundSprite((x * tile_size , y * tile_size), image, self.all_sprites, scale)

        for obj in map.get_layer_by_name('Tents'):
            CollisionSprite((obj.x * scale, obj.y * scale), obj.image, (self.all_sprites, self.collision_sprites), scale)
        
        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x * scale, obj.y * scale), obj.image, (self.all_sprites, self.collision_sprites), scale, obj.name)
            
        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x * scale, obj.y * scale), self.all_sprites, self.collision_sprites)

    def loadIntro(self):
        self.success, self.video_image = self.game_intro.read()

        if self.success:
            height, width = self.video_image.shape[:2]
            video_surf = pygame.image.frombuffer(self.video_image.tobytes(), (width, height), "BGR")
            video_surf = pygame.transform.scale(video_surf, (1280, 720))
            self.display_surface.blit(video_surf, (0, 0))

    def handle_menu_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        for sprite in self.menu_sprites:
            if sprite.rect.collidepoint(mouse_pos) and mouse_pressed and not self.success:
                if sprite.name == "Start":
                    self.main_menu = False
                    self.game_intro.release()
                    break
                elif sprite.name == "Exit":
                    self.running = False
                    print("Exiting...")
                    break

            if isinstance(sprite, MenuButton) and not self.success:
                self.display_surface.blit(sprite.text, sprite.text_rect)


    def run(self):
        previous_time = time.time()
            
        while self.running:
            delta_time = time.time() - previous_time
            previous_time = time.time() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill((255, 255, 255))

            if not self.main_menu:
                keys = pygame.key.get_pressed()
                self.player.movement(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d], delta_time, self.FPS)

                # game progression
                # for sprites in self.collision_sprites:
                #     if sprites.name == "Gate 2":
                #         sprites.kill()

                self.all_sprites.draw(self.player.rect.center)
                # self.display_surface.blit(self.inventory_bar.image, self.inventory_bar.rect)
                self.inventory_bar.draw()
                self.inventory_bar.add_item(Item((self.inventory_bar.rect.left + 60, self.inventory_bar.rect.centery + 10), self.inventory_bar.items, 1))
                self.inventory_bar.add_item(Item((self.inventory_bar.rect.left + 160, self.inventory_bar.rect.centery + 10), self.inventory_bar.items, 2))


                
            else:
                self.menu_sprites.draw(self.display_surface)
                self.loadIntro()
                self.handle_menu_buttons()              

            pygame.display.flip()
            self.clock.tick(self.introFPS if self.success else self.FPS)


        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()