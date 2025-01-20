import pygame # type: ignore

class InventoryBar():
    def __init__(self, pos):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('design/inventory/inventory bar.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        # For controlling the items
        self.item_list = []

        # Create item holders
        self.item_holders = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        self.create_item_holders()

    def add_item(self, item_id):
        self.item_list.append(item_id)

    def drawItems(self, item_list):
        for i, item in enumerate(item_list):
            Item((self.rect.left + 60 + i * 100, self.rect.centery + 10), self.items, item) # i love this AI

    def drawHolders(self):
        for item_holder in self.item_holders:
            self.display_surface.blit(item_holder.image, item_holder.rect)

    def draw(self):
        self.display_surface.blit(self.image, self.rect)
        self.drawHolders()
        self.drawItems(self.item_list)

        for item in self.items:
            self.display_surface.blit(item.image, item.rect)
      
    
    def create_item_holders(self):
        for i in range(3):
            ItemHolder((self.rect.left + 60 + i * 100, self.rect.centery + 10), self.item_holders)
   
class ItemHolder(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('design/inventory/ItemHolder.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups, item_id):
        super().__init__(groups)
        image_path = f'design/inventory/items/{item_id}.png'
        default_image_path = 'design/inventory/items/1.png'
    
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load(default_image_path).convert_alpha()

        self.rect = self.image.get_rect(center=pos)
        self.item_id = item_id
