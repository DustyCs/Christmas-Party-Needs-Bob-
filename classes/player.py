"""
    Player = Bob

    Bob needs control.
    Bob needs to be able to smile.
    ...

    TODO

    Need to load appropriate image when player is moving. Currently Bob has one used for all directions
    Add slime like animation for Bob

    Stop Bob from going outside the computer screen!
    Bob is leaving a trail behind 0 o 0 - clean it! - Animations are images - Bob is an image that keeps getting drawn
    Bob is sad about being too big :( - Rescale him

"""

class Player:
    player_image = None
    player_rect = None
    player_speed = 5
    movement_state = "idle"
    animation_frame = 0

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
            # self.movement_state = "side"
        if K_d:
            self.player_rect.x += self.player_speed
            self.movement_state = "side"
        if K_w:
            self.player_rect.y -= self.player_speed
            self.movement_state = "up"
        if K_s:
            self.player_rect.y += self.player_speed
            self.movement_state = "down"

    def render(self, window):
        window.fill((0, 0, 0))
        window.blit(self.side_imgs[self.animation_frame], self.player_rect)
        self.animation_frame += 1
        print(self.animation_frame)
        if self.animation_frame >= 3:
            self.animation_frame = 0
        # window.blit(self.player_image, self.player_rect)

        # if self.movement_state == "side":
        #     for x in range(len(self.side_imgs)):
        #         window.fill((0, 0, 0))                
        #         window.blit(self.side_imgs[x], self.player_rect)
