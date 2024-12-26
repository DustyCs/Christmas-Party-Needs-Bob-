import pygame

class Background():
    testSurface = pygame.Surface([500, 500])
    testSurface_rect = testSurface.get_rect()
    testSurface.fill((100, 255, 100))

    background_image = None
    background_rect = None
    width = None
    height = None

    lastPos = None

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

    def testDraw(self):
        pass

    def render(self, window, player_offset, player_velocity):
        self.player_offset = player_offset # add for collisions
        self.player_x = player_offset.x + 64 #player height
        self.player_y = player_offset.y + 64

        player_passed = False
        cancel_movement = 0
        player_pos = self.background_rect.x - self.player_x
    
        
    
        print(self.background_rect.x - self.player_x) # x will not never change because its not being actually change but just the place its being drawn by the blit
        
        # Check if player passed this x value then cancel out
        if(player_pos >= 0 or player_pos <= -1280):
            player_passed = True
            # print("tru")
        else:
            player_passed = False


        # if player_passed:
        #     cancel_movement = player_offset.x
        #     print(self.background_rect.x)
        # else:
        #     cancel_movement = 0
        
        # Works

        if not player_passed:
            window.blit(self.background_image, (self.background_rect.x - self.player_x, self.background_rect.y - self.player_y))
            self.lastPos = self.background_rect.x - self.player_x
            print(self.lastPos)
        else:
            print(self.lastPos)
            window.blit(self.background_image, (self.lastPos, self.background_rect.y - self.player_y))
        # else:
        #     window.blit(self.background_image, (self.background_rect.x, self.background_rect.y - self.player_y))