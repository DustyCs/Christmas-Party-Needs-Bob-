import pygame # type: ignore
import time
from utils.decorators import *

class Player(pygame.sprite.Sprite):
    player_speed = 10
    player_velocity = None

    attack_key = None

    movement_state = "idle"
    animation_direction = None

    animation_speed= 0.2
    animation_frame = 0
    frame_x = 0
    frame_y = 0

    last_idle = time.time()

    def __init__(self, groups, collision_sprites):
        super().__init__(groups)
        self.player_sprite_idle = pygame.image.load('design/Slime/Idle/Slime1_Idle_full.png').convert_alpha()
        self.player_sprite_run = pygame.image.load('design/Slime/Run/Slime1_Run_full.png').convert_alpha()
        self.image_scale = 1
        self.image_size = 64
        self.image = self.getImage(self.player_sprite_idle, self.frame_x, self.frame_y, self.image_size, self.image_size, self.image_scale, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 600, 235
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()

    def movement(self, K_w, K_a, K_s, K_d, delta_time, FPS):
        self.direction.x = int(K_d - int(K_a))
        self.direction.y = int(K_s - int(K_w))

        print(self.direction)

        if self.movement_state == "idle":
            self.idleAnimation()
        if self.movement_state == "run":
            self.runAnimation(self.animation_direction)
        self.player_velocity = self.player_speed * delta_time * FPS   
        self.rect.center += self.direction * self.player_velocity

        if K_a:
            self.movement_state = "run"
            self.animation_direction = "left"
            self.collision('horizontal')
            self.frame_x = int(self.frame_x) + 1
        elif K_d:
            self.movement_state = "run"
            self.animation_direction = "right"
            self.collision('horizontal')
            self.frame_x = int(self.frame_x) + 1
        elif K_w:
            self.movement_state = "run"
            self.animation_direction = "up"
            self.collision('vertical')
            self.frame_x = int(self.frame_x) + 1
        elif K_s:
            self.movement_state = "run"
            self.animation_direction = "down"
            self.collision('vertical')
            self.frame_x = int(self.frame_x) + 1
        else:
            self.movement_state = "idle"


        if self.attack_key:
            pass
    
    def collision(self, direction):
        print(direction)
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top

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
        
        self.image = self.getImage(self.player_sprite_idle, converted_frame, self.frame_y, self.image_size, self.image_size, self.image_scale, (0,0,0))

        if self.frame_y <= 3 and converted_frame >= 5:
            self.frame_y += 1
        if self.frame_y == 4 and converted_frame >= 5:
            self.frame_y = 0
        if converted_frame >= 5:
            self.frame_x = 0

    def runAnimation(self, direction):
        self.image = self.getImage(self.player_sprite_run, self.frame_x, self.frame_y, self.image_size, self.image_size, self.image_scale, (0,0,0))
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

    def knockbackCollision(self):
        self.rect.x += self.player_velocity # only one true to eject the player until its false
