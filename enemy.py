from game import *

class Enemy(pygame.sprite.Sprite):
    """ The enemy who shoots the player """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 2
            
    def update(self):
        self.rect.x += self.speedx
        
        if self.rect.left < 0:
            self.speedx *= -1
            self.rect.y += 60
        if self.rect.right > WIDTH:
            self.speedx *= -1
            self.rect.y += 60
            