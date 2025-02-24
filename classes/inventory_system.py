import pygame # type: ignore

#----------------------------------------------------------------
# Inventory System
# 
# Link to item functions
from items.items import items as item_dict
#----------------------------------------------------------------

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
        self.selected_item = pygame.sprite.Group()

        self.create_item_holders()

    def remove_item(self, item_id):
        self.item_list.remove(item_id)
    
    def mouse_collision(self, mouse_pos):
        for item_holder in self.item_holders:
            if item_holder.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.selected_item.add(item_holder.onClick(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1), list(self.items)))
                    if len(self.selected_item) > 1:
                        self.selected_item.remove(self.selected_item.sprites()[0])

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

    def drawHolders(self):
        for item_holder in self.item_holders:
            self.display_surface.blit(item_holder.image, item_holder.rect)

    ###
    # This draw function overrides the sprite draw function
    # to draw items and item holders separately.
    ###
    def draw(self):
        self.display_surface.blit(self.image, self.rect)
        self.drawHolders()

        if self.item_list:
            self.drawItems(self.item_list)

        for item in self.items:
            self.display_surface.blit(item.image, item.rect)

        # Draw selected item in the middle of the screen
        for sprite in self.selected_item:
            # print(" selected item id is ", sprite.item_id)
            sprite_img = pygame.transform.scale(sprite.image, (sprite.rect.width * 0.5, sprite.rect.height * 0.5))
            sprite_pos = (1280/2 - sprite.rect.width/2 + 50, 720/2 - sprite.rect.height/2)
            
            itemFunction = item_dict.get(sprite.item_id)
            useItemFunction = itemFunction[2]
            useItemFunction(sprite)
            self.display_surface.blit(sprite_img, sprite_pos)
                  
            
            

         
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
                return item.onClick()
        

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


#----------------------------------------------------------------
# Inventory Interface
#----------------------------------------------------------------

class InventoryInterface():
    def __init__(self):
        self.image = pygame.image.load("design/inventory/inventory.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect(center=(1280/2, 720/2))
        self.inventory_slots = 10
        self.inventory_items = [ [""] for x in range(self.inventory_slots) ]
    
    def add_item(self, x, itemSprite):
            if x <= 10:
                self.inventory_items[x] = itemSprite

    def show_inventory(self):
        # print("toggled")
        self.display_surface = pygame.display.get_surface()
        self.display_surface.blit(self.image, self.rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]


        for i, item in enumerate(self.inventory_items):
            if item != [""]:
                image = pygame.transform.scale(item.image, (item.image.get_width() * 1, item.image.get_height() * 1))
                if i <= 5:
                    # self.display_surface.blit(image, (self.rect.left + 84 + i * 100, self.rect.top + 36))
                    item_position = (self.rect.left + 84 + i * 100, self.rect.top + 36)
                else:
                    # self.display_surface.blit(image, (self.rect.left + 84 + i * 100, self.rect.top + 36 + 58 + 58))
                    item_position = (self.rect.left + 84 + (i - 5) * 100, self.rect.top + 36 + 58 + 58)

                if item.rect.collidepoint(mouse_pos):
                    # print("collide")
                    if mouse_pressed:
                        item.clicked = not item.clicked

                # Click and Drag
                if not item.clicked:
                    item.rect.topleft = item_position
                if item.clicked:
                    print("clicked")
                    item.rect.topleft = (mouse_pos[0] - item.rect.width/2, mouse_pos[1] - item.rect.height/2)

                self.display_surface.blit(image, item.rect.topleft)

                print(item.clicked)
                        
                

    
       

              
            