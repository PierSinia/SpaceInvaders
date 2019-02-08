from game import *

# TODO: Animate the enemy images.

class Enemy(pygame.sprite.Sprite):
    """ The enemy who shoots the player """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.enemyIMG = pygame.image.load("img/alien1.png")
        self.image = pygame.transform.scale(self.enemyIMG, (35, 26))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 1.0
            
    def update(self):
        self.rect.x += self.speedx
    
 