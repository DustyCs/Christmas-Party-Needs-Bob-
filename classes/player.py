"""
    Player = Bob

    Bob needs control.
    Bob needs to be able to smile.
    ...

    TODO

    Need to load appropriate image when player is moving. Currently Bob has one used for all directions
    Add slime like animation for Bob

    Stop Bob from going outside the computer screen!
    Bob is leaving a trail behind 0 o 0 - clean it! - Hint: Animations are images - Bob is an image that keeps getting drawn
    Bob is sad about being too big :( - Rescale him

"""

class Player:
    player_image = None
    player_rect = None
    player_speed = 5

    def __init__(self, image, player_rect):
        self.player_image = image
        self.player_rect = player_rect

    def testPrint(self): # The function you use when ya don't know what's up with the properties and methods
        print(self.player_rect) # Why is pygame ce being weird with cols?

    def movement(self, K_w, K_a, K_s, K_d):
        if K_a:
            self.player_rect.x -= self.player_speed
        if K_d:
            self.player_rect.x += self.player_speed
        if K_w:
            self.player_rect.y -= self.player_speed
        if K_s:
            self.player_rect.y += self.player_speed

    def render(self, window):
        window.blit(self.player_image, (self.player_rect.x, self.player_rect.y)) # CB func example