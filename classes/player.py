import pygame # type: ignore

class Player():
    player_image = None
    player_sprite_idle = None
    player_rect = None
    player_speed = 10
    movement_state = "idle"

    animation_frame = 0
    frame_x = 0
    frame_y = 0

    def __init__(self):
        pass

    def testPrint(self): # The function you use when ya don't know what's up with the properties and methods
        print(self.player_rect) 

    def movement(self, K_w, K_a, K_s, K_d, delta_time, FPS):
        # print(self.player_speed * delta_time * FPS)
        if K_a:
            self.player_rect.x -= self.player_speed * delta_time * FPS
            self.movement_state = "side" 
        if K_d:
            self.player_rect.x += self.player_speed * delta_time * FPS
            self.movement_state = "side"
        if K_w:
            self.player_rect.y -= self.player_speed * delta_time * FPS
            self.movement_state = "up"
        if K_s:
            self.player_rect.y += self.player_speed * delta_time * FPS
            self.movement_state = "down"

        self.idleAnimation()
        
    def getImage(self, sheet, frame_x, frame_y, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image_base = 64
        image.blit(sheet, (0, 0), ((width * frame_x), (image_base * frame_y), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
    def idleAnimation(self):
        animation_speed = 0.2 # this only works with numbers that is a factor of 10!~
        self.frame_x += animation_speed 
        self.player_image = self.getImage(self.player_sprite_idle, int(self.frame_x), self.frame_y, 64, 64, 2, (0,0,0))
        print(self.frame_x, self.frame_y)

        if self.frame_y <= 3 and int(self.frame_x) >= 5:
            self.frame_y += 1
        if self.frame_y == 4 and int(self.frame_x) >= 5:
            self.frame_y = 0
        if int(self.frame_x) == 5:
            self.frame_x = 0

    def render(self, window):
        window.blit(self.player_image, self.player_rect)
