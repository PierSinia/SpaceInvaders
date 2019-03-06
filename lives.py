from game import *

class Lives(object):
    def __init__(self, max):
        #Max = max lives
        self.current = max
        self.gap = 35
        self.x = 10 #prefer
        self.y = 10 #prefer
        self.player_img = pygame.image.load("img/Laser_Cannon.png")
        self.image = pygame.transform.scale(self.player_img, (30, 30))

    def draw(self, surface):
        for i in range(self.current):
            surface.blit(self.image,(self.x + (i * self.gap), self.y))