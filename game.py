import pygame
import time
import random
import sys
from settings import *
from player import Player
from enemybullet import EnemyBullet
from playerbullet import PlayerBullet
from enemy import Enemy
from obstacle import Obstacle
from lives import Lives

class Game(object):
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
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.lives = Lives(3)


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
            self.enemy_shoot()
            self.draw()
        
        quit()
        pygame.quit()
        sys.exit()

    def player_shoot(self):
        """ Make the player shoot bullets """
        self.playerbullet = PlayerBullet(self.player.rect.centerx, self.player.rect.top, -10, YELLOW)
        self.all_sprites.add(self.playerbullet)
        self.player_bullets.add(self.playerbullet)
    
    """ draw lives """

    def enemy_shoot(self):
        self.shooting_chance = 1400
        for enemy in self.enemies:
            # Have a random chance of shooting each frame
            if random.randrange(self.shooting_chance) == 0:
                self.enemy_bullet = EnemyBullet(enemy.rect.centerx, enemy.rect.bottom, 10, RED)
                self.all_sprites.add(self.enemy_bullet)
                self.enemy_bullets.add(self.enemy_bullet)

    def events(self):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player_shoot()
            
    def update(self):
        # Game loop - update
        """ update all the sprites """
        self.all_sprites.update()
        self.playerbulletEnemyHit = pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, True)
        self.PlayerObstacle_hit = pygame.sprite.groupcollide(self.player_bullets, self.obstacles, True, True)
        self.enemybulletObstacle_hit = pygame.sprite.groupcollide(self.enemy_bullets, self.obstacles, True, True)
        self.enemybulletPlayer_hit = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
        if self.enemybulletPlayer_hit:
            self.player.rect.x = WIDTH /2
            self.lives.current -= 1

        if self.lives.current == 0:
            self.running = False
        
        """make all the enemies bounce when one hits the edge"""
        for oneEnemy in self.enemies:
            if oneEnemy.rect.right > WIDTH: # if one hits the edge
                for allEnemies in self.enemies: # Change the direction of all the enemies
                    allEnemies.rect.y += 5
                    allEnemies.speedx *= -1.0
                break

            elif oneEnemy.rect.left < 0: # if one hits the edge
                for allEnemies in self.enemies: # Change the direction of all the enemies
                    allEnemies.speedx *= -1.0
                    allEnemies.rect.y += 5
                break

    def draw(self):
        self.backgroundrect = self.background.get_rect()
        self.screen.blit(self.background, self.backgroundrect)
        self.all_sprites.draw(self.screen)
        self.lives.draw(self.screen)
        """ Update the screen when everything has been drawn """
        pygame.display.flip()
