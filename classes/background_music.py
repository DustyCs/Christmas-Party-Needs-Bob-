import pygame #type: ignore
import os
from pygame import mixer #type: ignore

mixer.init()

class areaBGM(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, file, name, groups, scale):
        super().__init__(groups)
        self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(self.image, (width * scale, height * scale))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.file = "audio/music/" + file + ".mp3"
        self.audio_file = pygame.mixer.Sound(self.file)
        self.name = name

    def play(self):
        self.audio_file.play(loops=-1)
        cwd = os.getcwd()
        print(cwd)
    
    def stop(self):
        self.audio_file.stop()