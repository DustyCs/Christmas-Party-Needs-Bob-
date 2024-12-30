import pygame

class Background():
    background_image = None
    background_rect = None
    width = None
    height = None

    lastPos = None
    lastPosY = None

    objects = []
    object_converted = []
    objects_rect = []

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

    def createObject(self, w, h, x, y): 
        objectSurface = pygame.Surface([w, h]).convert_alpha() 
        object_rect = objectSurface.get_rect()
        object_rect.x, object_rect.y = x, y
 
        return [objectSurface, object_rect]

    def antiMoveObject(self, object, x, y):
        if object.x >= x:
            object.x = x 
        if object.y >= y:
            object.y = y

    def objectScroll(self, object, width):
        object.x -= self.player_offset.x - width
        object.y -= self.player_offset.y

    def drawObjects(self):
        self.object_converted = [self.createObject(x[0][0], x[0][1], x[1], x[2]) for x in self.objects] # whats x?
        self.objects_rect = [ x[1] for x in self.object_converted]

        # for x in range(len(self.objects_rect)):
        #     self.objectScroll(self.objects_rect[x], self.objects[x][0][0]) # width
        #     self.antiMoveObject(self.objects_rect[x], self.objects[x][1], self.objects[x][2]) # x, y

        # self.objectScroll(self.objects_rect[1], 500)
        # self.antiMoveObject(self.objects_rect[1], 200, 700)

        self.objects_rect[1].x -= self.player_offset.x
        self.objects_rect[1].y -= self.player_offset.y

        print(self.objects_rect[1].x)

        if self.objects_rect[1].x >= 240:
            self.objects_rect[1].x = 240 
            print("rtue")

        # if self.objects_rect[1].y >= 700:
        #     self.objects_rect[1].y = 700

        self.objectScroll(self.objects_rect[0], 240)
        self.antiMoveObject(self.objects_rect[0], 140, 400)

        self.object_converted[1][0].fill((0, 0, 0))

        # print(self.objects_rect[1])

    def render(self, window, player_offset):
        self.player_offset = player_offset # add for collisions
        self.player_x = player_offset.x + 64 #player height
        self.player_y = player_offset.y + 64

        player_posx = self.background_rect.x - self.player_x
        player_posy = self.background_rect.y - self.player_y

      
        # collision

        # Scroll

            # Background Scroll
        if not ((player_posx >= 0 or player_posx <= -1280) or (player_posy >= 0 or player_posy <= -720)):
            window.blit(self.background_image, (self.background_rect.x - self.player_x, self.background_rect.y - self.player_y))
            self.lastPos = self.background_rect.x - self.player_x
            self.lastPosY = self.background_rect.y - self.player_y
        elif self.player_x >= 0 and not (player_posy >= 0 or player_posy <= -720):
            window.blit(self.background_image, (self.lastPos, self.background_rect.y - self.player_y))
            self.lastPosY = self.background_rect.y - self.player_y
        elif self.player_y >= 0 and not (player_posx >= 0 or player_posx <= -1280):
            window.blit(self.background_image, (self.background_rect.x - self.player_x, self.lastPosY))
            self.lastPos = self.background_rect.x - self.player_x
        else:
            window.blit(self.background_image, (self.lastPos, self.lastPosY))
            # print("true")


        # Objects Scroll
        self.drawObjects()



        # window.blit(self.object_converted[0][0], (self.objects_rect[0].x, self.objects_rect[0].y))

        # test

        window.blit(self.object_converted[1][0], (self.objects_rect[1].x, self.objects_rect[1].y))
        pygame.draw.rect(window, (0, 255, 0), self.objects_rect[0]) 
        pygame.draw.rect(window, (0, 255, 0), self.objects_rect[1]) 
        # issue with rect moving after 140, 400 (x, y)

        # Rect(x, y, width, height)
        # Player
        pygame.draw.rect(window, (0, 255, 0), self.player_offset)
