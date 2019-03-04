from game import *

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedy, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 25))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = speedy
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
