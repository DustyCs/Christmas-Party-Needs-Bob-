import pygame # type: ignore

class InventoryBar():
    def __init__(self, pos):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('design/inventory/inventory bar.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        # For controlling the items
        self.item_list = []
        self.current_items = []

        # Create item holders
        self.item_holders = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        self.create_item_holders()

    def remove_item(self, item_id):
        self.item_list.remove(item_id)
    
    def mouse_collision(self, mouse_pos):
        for item_holder in self.item_holders:
            if item_holder.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    item_holder.onClick(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1), list(self.items))
                return item_holder

    def add_item(self, item_id):
        if item_id not in self.item_list and len(self.item_list) < 3:
            self.item_list.append(item_id)
            print(f"Added item: {item_id}. Current item_list: {self.item_list}")  # Add this line


    def drawItems(self, item_list):
        self.items.empty()
        self.current_items = []

        for i, item in enumerate(item_list):
            if i < 3:  # Limit to 3 items
                new_item = Item((self.rect.left + 60 + i * 100, self.rect.centery + 10), (self.items), item)
                self.current_items.append(new_item)
        
        
        self.mouse_collision(pygame.mouse.get_pos())

    # test

    def draw(self):
        # self.display_surface.blit(self.image, self.rect)
        self.drawHolders()

        if self.item_list:
            self.drawItems(self.item_list)

        for item in self.items:
            self.display_surface.blit(item.image, item.rect)

    def draw_clicked_item(self, item):
        # Draw the clicked item on top of everything else
        self.display_surface.blit(item.image, item.rect)



    def drawHolders(self):
        for item_holder in self.item_holders:
            self.display_surface.blit(item_holder.image, item_holder.rect)

    def draw(self):
        self.display_surface.blit(self.image, self.rect)
        self.drawHolders()

        if self.item_list:
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

    def onClick(self, event, item_group):
        # print(f'Clicked on item holder {item_group}')
        for item in item_group:
            if pygame.mouse.get_pressed()[0] and item.rect.collidepoint(pygame.mouse.get_pos()):
                print(f'Clicked on item {item.onClick()}')

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
        self.clicked = False


    def onClick(self):
        print(f'Clicked on item {self.item_id}')
        self.clicked = not self.clicked
        return self

    def drawItem(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.blit(self.image, self.rect)
