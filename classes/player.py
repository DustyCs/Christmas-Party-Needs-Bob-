import pygame # type: ignore

class Player:
    player_image = None
    player_sprite_idle = None
    player_rect = None
    player_speed = 5
    movement_state = "idle"
    animation_frame = 0

    image = None
    frame_x = 0
    frame_y = 1

    side_imgs = []
    up_imgs = []
    down_imgs = []

    def __init__(self):
        pass

    def testPrint(self): # The function you use when ya don't know what's up with the properties and methods
        print(self.player_rect) # Why is pygame ce being weird with cols?

    def movement(self, K_w, K_a, K_s, K_d):
        if K_a:
            self.player_rect.x -= self.player_speed
            self.movement_state = "side" 
            self.animation_frame += 1 # this would not reset if called in another key - need fix
            if self.animation_frame >= 3: # this
                self.animation_frame = 0 # this
        if K_d:
            self.player_rect.x += self.player_speed
            self.movement_state = "side"
            self.animation_frame += 1 
            if self.animation_frame >= 3:
                self.animation_frame = 0
        if K_w:
            self.player_rect.y -= self.player_speed
            self.movement_state = "up"
            self.animation_frame += 1 
            if self.animation_frame >= 5:
                self.animation_frame = 0
        if K_s:
            self.player_rect.y += self.player_speed
            self.movement_state = "down"
            self.animation_frame += 1 
            if self.animation_frame >= 5:
                self.animation_frame = 0

    def getImage(self, sheet, frame_x, frame_y, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image_base = 64
        image.blit(sheet, (0, 0), ((width * frame_x), (image_base * frame_y), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    def render(self, window):
        # window.fill((0, 0, 0))
        # window.blit(self.player_sprite_idle, (0, 0))
        window.blit(self.getImage(self.player_sprite_idle, self.frame_x, self.frame_y, 64, 64, 3, (0,0,0)), self.player_rect)





        # window.blit(self.player_image, self.player_rect)






        # need cleaning and fixing - DRY - also reset the animation frame
        # scrapped
        # could be useful though
        # if self.movement_state == "side":
        #     window.fill((0, 0, 0))                
        #     window.blit(self.side_imgs[self.animation_frame], self.player_rect)
        # if self.movement_state == "up":
        #     window.fill((0, 0, 0))                
        #     window.blit(self.up_imgs[self.animation_frame], self.player_rect)
        # if self.movement_state == "down":
        #     window.fill((0, 0, 0))                
        #     window.blit(self.down_imgs[self.animation_frame], self.player_rect)
