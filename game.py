import pygame
import time
import random
import sys
from settings import *
from player import Player
from bullet import Bullet
from enemy import Enemy

class Game:
    """ Game class - game logic """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True
        self.background = pygame.image.load("img/spaceInvadersBG.jpg").convert()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.bullets = pygame.sprite.Group()
        #self.bullets.add()


        """ Making the rows of enemies """
        for b in range(5): # 5 vertical rows of enemies
            self.xPos = 100 # Original starting x position
            for i in range(11): # 11 horizontal rows of enemies
                self.e = Enemy(self.xPos, 40 + (50 * b)) # Spawning an enemy
                self.all_sprites.add(self.e) # Adding it to the all_sprites group
                self.enemies.add(self.e) # Adding it to the enemies group
                self.xPos += 50 # Change x position every time with the same value when a new enemy has been made
                

        # Game Loop
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        quit()
        pygame.quit()
        sys.exit()

    def shoot(self):

        """ Make the player shoot bullets """
        self.bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
        self.all_sprites.add(self.bullet)
        self.bullets.add(self.bullet)
    
    def events(self):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shoot()

    def update(self):

        # Game loop - update
        """ update all the sprites """
        self.all_sprites.update()
        
        self.PlayerBullet_hit = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        self.touchedRight = False
        self.touchedLeft = False
        """make all the enemies bounce when one hits the edge"""
        for oneEnemy in self.enemies:
            if oneEnemy.rect.right > WIDTH and self.touchedRight == False:
                self.touchedRight = True 
                for allEnemies in self.enemies: # Change the direction of all the enemies
                    allEnemies.rect.y += 5
                    allEnemies.speedx *= -1
            
            if oneEnemy.rect.left < 0 and self.touchedLeft == False: # if one hits the edge ...
                self.touchedLeft = True
                for allEnemies in self.enemies:# and self.touched_left == False: # Change the direction of all the enemies
                    allEnemies.speedx *= -1
                    allEnemies.rect.y += 5
            
    def draw(self):
        self.backgroundrect = self.background.get_rect()
        self.screen.blit(self.background, self.backgroundrect)
        self.all_sprites.draw(self.screen)
        self.bullets.draw(self.screen)
        """ Update the screen when everything has been drawn """
        pygame.display.flip()
