import pygame
import time
import random
import sys
from settings import *
from player import Player
from bullet import Bullet
from enemy import Enemy
from obstacle import Obstacle

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
        self.obstacles = pygame.sprite.Group()

        """ Making the rows of enemies """
        for b in range(5): # 5 vertical rows of enemies
            self.xPos = 100 # Original starting x position
            for i in range(11): # 11 horizontal rows of enemies
                self.e = Enemy(self.xPos, 40 + (30 * b)) # Spawning an enemy
                self.all_sprites.add(self.e) # Adding it to the all_sprites group
                self.enemies.add(self.e) # Adding it to the enemies group
                self.xPos += 50 # Change x position every time with the same value when a new enemy has been made
        
        """ drawing the obstacles """
        # TODO: make the code shorter
        for b in range(5): 
            self.xPos = (WIDTH * (1/3)) - 70
            for i in range(7): # 
                self.obstacle = Obstacle(self.xPos, HEIGHT - 140+ (10 * b)) # 
                self.all_sprites.add(self.obstacle) # Adding it to the all_sprites group
                self.obstacles.add(self.obstacle) 
                self.xPos += 10 
        for b in range(5): 
            self.xPos = (WIDTH / 2) - 35 
            for i in range(7): # 
                self.obstacle = Obstacle(self.xPos, HEIGHT - 140+ (10 * b)) # 
                self.all_sprites.add(self.obstacle) # Adding it to the all_sprites group
                self.obstacles.add(self.obstacle) 
                self.xPos += 10 
    
        for b in range(5): 
            self.xPos = WIDTH * (2/3)
            for i in range(7): # 
                self.obstacle = Obstacle(self.xPos, HEIGHT - 140+ (10 * b)) # 
                self.all_sprites.add(self.obstacle) # Adding it to the all_sprites group
                self.obstacles.add(self.obstacle) 
                self.xPos += 10 

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
        self.PlayerObstacle_hit = pygame.sprite.groupcollide(self.bullets, self.obstacles, True, True)
        self.touchedRight = False
        self.touchedLeft = False
        """make all the enemies bounce when one hits the edge"""
        for oneEnemy in self.enemies:
            if oneEnemy.rect.right > WIDTH * 0.95 and self.touchedRight == False: # if one hits the edge and it hasn't hit the edge already
                self.touchedRight = True # Set the touchedRight edge boolean to True because it touched the edge now
                for allEnemies in self.enemies: # Change the direction of all the enemies
                    allEnemies.rect.y += 25
                    allEnemies.speedx *= -1
            
            if oneEnemy.rect.left < WIDTH * 0.05 and self.touchedLeft == False: # if one hits the edge and it hasn't hit the edge already
                self.touchedLeft = True # Set the touchedLeft edge boolean to True because it touched the edge now
                for allEnemies in self.enemies: # Change the direction of all the enemies
                    allEnemies.speedx *= -1
                    allEnemies.rect.y += 25

    def draw(self):
        self.backgroundrect = self.background.get_rect()
        self.screen.blit(self.background, self.backgroundrect)
        self.all_sprites.draw(self.screen)

        """ Update the screen when everything has been drawn """
        pygame.display.flip()
