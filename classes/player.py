import pygame # type: ignore
import time
from utils.decorators import *

class Player():
    player_image = None
    player_sprite_idle = None
    player_sprite_run = None
    player_rect = None
    player_speed = 10
    player_velocity = None

    attack_key = None

    movement_state = "idle"
    direction = None

    animation_speed= 0.2
    animation_frame = 0
    frame_x = 0
    frame_y = 0

    last_idle = time.time()

    def __init__(self):
        pass

    def movement(self, K_w, K_a, K_s, K_d, delta_time, FPS):
        """ 
          
        Cleaaaaaaaaaan       

        """

        if self.movement_state == "idle":
            self.idleAnimation()
        if self.movement_state == "run":
            self.runAnimation(self.direction)

        self.player_velocity = self.player_speed * delta_time * FPS   
        
        # A VERY DRY PROBLEM

        if K_a:
            self.player_rect.x -= self.player_velocity
            self.movement_state = "run"
            self.direction = "left"
            self.frame_x = int(self.frame_x) + 1

        elif K_d:
            self.player_rect.x += self.player_velocity
            self.movement_state = "run"
            self.direction = "right"
            self.frame_x = int(self.frame_x) + 1

        elif K_w:
            self.player_rect.y -= self.player_velocity
            self.movement_state = "run"
            self.direction = "up"
            self.frame_x = int(self.frame_x) + 1

        elif K_s:
            self.player_rect.y += self.player_velocity
            self.movement_state = "run"
            self.direction = "down"
            self.frame_x = int(self.frame_x) + 1

        else:
            self.movement_state = "idle"


        if self.attack_key:
            pass
    
    def attack(self): pass
        
    def getImage(self, sheet, frame_x, frame_y, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image_base = 64
        image.blit(sheet, (0, 0), ((width * frame_x), (image_base * frame_y), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
    def setLastIdle(self): self.last_idle = time.time()

    def convertNextFrame(self, x): return int(x) + 1

    def idleAnimation(self):
        self.frame_x += self.animation_speed 
        converted_frame = int(self.frame_x) 
        
        self.player_image = self.getImage(self.player_sprite_idle, converted_frame, self.frame_y, 64, 64, 2, (0,0,0))

        if self.frame_y <= 3 and converted_frame >= 5:
            self.frame_y += 1
        if self.frame_y == 4 and converted_frame >= 5:
            self.frame_y = 0
        if converted_frame >= 5:
            self.frame_x = 0

    def runAnimation(self, direction):
        self.player_image = self.getImage(self.player_sprite_run, self.frame_x, self.frame_y, 64, 64, 2, (0,0,0))
        converted_frame = int(self.frame_x) 
        self.frame_y = 3
     
        if converted_frame >= 7:
            self.frame_x = 0

        match direction:
            case "left":
                self.frame_y = 2
            case "right":
                self.frame_y = 3
            case "up":
                self.frame_y = 1
            case "down":
                self.frame_y = 0
      
    def attackAnimation(self):
        pass

    def render(self, window):
        window.blit(self.player_image, self.player_rect)
