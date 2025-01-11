import pygame # type: ignore

class MainMenu(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('design/Main Menu/Main Menu.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect()
        self.name = "Main Menu"
        self.options = ["Start", "Options", "Exit"]
        self.BUTTON_POSITIONS = [(300, 600), (500, 600), (700, 600)]

        self.createButtons(groups)

    def createButtons(self, groups):
        for x in range(len(self.options)):
            MenuButton(self.BUTTON_POSITIONS[x], 'design/Main Menu/MenuButton.png', self.options[x], groups)

class MenuButton(pygame.sprite.Sprite):
    def __init__(self, pos, image, name, groups):
        super().__init__(groups)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.name = name
