import pygame #type: ignore
from classes.player import Player
from classes.inventory_system import Item, InventoryBar


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface() # gets the surface from anywhere in the loop
        self.offset = pygame.Vector2()

    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - (1280/2)) # 1280 - window width
        self.offset.y = -(target_pos[1] - (720/2))  # yes its the height

        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]


        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

        

        # get player pos

        # for key in object_sprites:
        #     # print(type(key))
        #     if isinstance(key, Player):
            #    print(key.hitbox_rect)
            #    pygame.draw.rect(self.display_surface, (0, 255, 255), (100, 100, key.hitbox_rect[2], key.hitbox_rect[3])) # x, y, width height

          