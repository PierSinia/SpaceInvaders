from game import *

class Player(pygame.sprite.Sprite):
    """ The main player who shoots the enemies """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_img = pygame.image.load("img/Laser_Cannon.png")
        self.image = pygame.transform.scale(self.player_img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 30
            
    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 4
        if key[pygame.K_RIGHT]:
            self.rect.x += 4

        """ Player can't go off the screen """
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx
        