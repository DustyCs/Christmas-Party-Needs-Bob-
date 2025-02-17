import pygame #type: ignore
from classes.player import Player
from classes.inventory_system import Item, InventoryBar


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface() # gets the surface from anywhere in the loop
        self.offset = pygame.Vector2()

        self.inventory_bar = None  # We'll set this from the main game loop
        self.clicked_item = None  # To store the currently clicked item

    def set_inventory_bar(self, inventory_bar):
        self.inventory_bar = inventory_bar

    def set_clicked_item(self, item):
        self.clicked_item = item


    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - (1280/2)) # 1280 - window width
        self.offset.y = -(target_pos[1] - (720/2))  # yes its the height

        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]
        clicked_items = [sprite for sprite in self if isinstance(sprite, Item) and sprite.clicked]


        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
                if sprite not in clicked_items:  # Don't draw clicked items here
                    self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

         # Draw clicked items last, so they appear on top
        for item in clicked_items:
            print("true")
            self.display_surface.blit(item.image, item.rect.topleft + self.offset)

          # Draw the inventory bar
        if self.inventory_bar:
            self.inventory_bar.draw()

        # Draw the clicked item on top if there is one
        if self.clicked_item:
            self.inventory_bar.draw_clicked_item(self.clicked_item)


        # # Reset clicked state after drawing
        # for item in clicked_items:
        #     item.clicked = False


        

        # get player pos

        # for key in object_sprites:
        #     # print(type(key))
        #     if isinstance(key, Player):
            #    print(key.hitbox_rect)
            #    pygame.draw.rect(self.display_surface, (0, 255, 255), (100, 100, key.hitbox_rect[2], key.hitbox_rect[3])) # x, y, width height

          