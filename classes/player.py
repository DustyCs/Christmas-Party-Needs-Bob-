import pygame # type: ignore

class Player():
    player_image = None
    player_sprite_idle = None
    player_sprite_run = None
    # player_sprite_walk_right = None
    # player_sprite_walk_top = None
    # player_sprite_walk_bottom = None
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
        if self.movement_state == "idle":
            self.idleAnimation()
        if self.movement_state == "run":
            self.runAnimation()
            
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
     
        
    def getImage(self, sheet, frame_x, frame_y, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image_base = 64
        image.blit(sheet, (0, 0), ((width * frame_x), (image_base * frame_y), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
    def idleAnimation(self):
        self.resetFrames()
        animation_speed = 0.2 # this only works with numbers that is a factor of 10!~
        self.frame_x += animation_speed 
        idle_frame = int(self.frame_x) # cleaner


        # test

        self.player_image = self.getImage(self.player_sprite_idle, idle_frame, self.frame_y, 64, 64, 2, (0,0,0))

        # self.player_image = self.getImage(self.player_sprite_idle, int(self.frame_x), self.frame_y, 64, 64, 2, (0,0,0)) R
        print(self.frame_x, self.frame_y)

        if self.frame_y <= 3 and idle_frame >= 5:
            self.frame_y += 1
        if self.frame_y == 4 and idle_frame >= 5:
            self.frame_y = 0
        if idle_frame == 5:
            self.frame_x = 0

    def runAnimation(self):
        self.player_image = self.getImage(self.player_sprite_run, int(self.frame_x), self.frame_y, 64, 64, 2, (0,0,0))

    
    def resetFrames(self):
        if self.frame_x < 0 or self.frame_y < 0:
         self.frame_x, self.frame_y = 0, 0

    def render(self, window):
        window.blit(self.player_image, self.player_rect)
