import pygame

class Background():
    background_image = None
    background_rect = None
    width = None
    height = None

    lastPos = None
    lastPosY = None

    objects = []

    player_offset = None # when checking for collision add this !
    player_x, player_y = None, None

    def __init__(self, image, pos_x, pos_y, scale=1):
        self.background_image = image
        self.height = self.background_image.get_height()
        self.width = self.background_image.get_width()
        self.background_image = pygame.transform.scale(self.background_image, ((self.width * scale),(self.height * scale) ) )
        self.background_rect = self.background_image.get_rect()
        self.background_rect.x = pos_x
        self.background_rect.y = pos_y

    def createObject(self, w, h):
        objectSurface = pygame.Surface([w, h])

        # Edit


        # Apply


        # Ouput

        return objectSurface

    def render(self, window, player_offset):
        self.player_offset = player_offset # add for collisions
        self.player_x = player_offset.x + 64 #player height
        self.player_y = player_offset.y + 64

        player_posx = self.background_rect.x - self.player_x
        player_posy = self.background_rect.y - self.player_y
        
        # Scroll
        print(self.player_x)
        if not ((player_posx >= 0 or player_posx <= -1280) or (player_posy >= 0 or player_posy <= -720)): # problem with scrolling again since it activates the else and stops the y scrolling
            window.blit(self.background_image, (self.background_rect.x - self.player_x, self.background_rect.y - self.player_y))
            self.lastPos = self.background_rect.x - self.player_x
            self.lastPosY = self.background_rect.y - self.player_y
        elif self.player_x >= 0 and not (player_posy >= 0 or player_posy <= -720):
            window.blit(self.background_image, (self.lastPos, self.background_rect.y - self.player_y))
            self.lastPosY = self.background_rect.y - self.player_y
        else:
            window.blit(self.background_image, (self.lastPos, self.lastPosY))
