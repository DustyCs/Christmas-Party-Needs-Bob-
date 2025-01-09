import pygame

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups, scale):
        super().__init__(groups)
        self.image = surface
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups, scale, name = None):
        super().__init__(groups)
        self.image = surface
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.rect = self.image.get_frect(topleft = pos)
        self.name = name