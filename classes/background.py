import pygame

class Background():
    testSurface = pygame.Surface([500, 500])
    testSurface_rect = testSurface.get_rect()
    testSurface.fill((100, 255, 100))

    background_image = None
    background_rect = None

    player_offset = None # when checking for collision add this !
    player_x, player_y = None, None

    def __init__(self, image, pos_x, pos_y, scale=1):
        self.background_image = image
        image_height = self.background_image.get_height()
        image_width = self.background_image.get_width()
        self.background_image = pygame.transform.scale(self.background_image, ((image_width * scale),(image_height * scale) ) )
        self.background_rect = self.background_image.get_rect()
        self.background_rect.x = pos_x
        self.background_rect.y = pos_y

    def testDraw(self):
        pass

    def render(self, window, player_offset):
        self.player_offset = player_offset
        self.player_x = player_offset.x
        self.player_y = player_offset.y



        # print(self.player_x, self.player_y)
        print(self.background_rect.x, self.background_rect.y)
        window.blit(self.background_image, (self.background_rect.x - self.player_x, self.background_rect.y - self.player_y))