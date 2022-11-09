import pygame as pg
import constants as k
import random as rn
from Ship.bullet import Bullet


class Ship(pg.sprite.Sprite):
    def __init__(self):
        super(Ship,self).__init__()
        #set the sprite (convert_alpha() allows to pygame to manipulate properly the image)
        self.image = pg.image.load('Ship\ship_sprite.png').convert_alpha()
        #reescale the sprite
        scaleFactor = 4
        self.image = pg.transform.scale(self.image, (self.image.get_width()*scaleFactor,self.image.get_height()*scaleFactor))

        #get the propierties as position form the object itself
        self.rect = self.image.get_rect()

        #initial position
        self.rect.x = k.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = k.DISPLAY_HEIGHT - self.rect.height


        #set the initial speed 
        self.vel_x = 0
        self.vel_y = 0
        #variaton of the speed when a key is press
        self.speed = 20

        self.bullets = pg.sprite.Group()
        self.isShooting = False
        self.shootingRate = 15


    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + self.rect.width //2 -2
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)

    def move_horizontal(self):
        if self.rect.x + self.vel_x < 0:
            self.rect.x = 0
        elif self.rect.x + self.vel_x > k.DISPLAY_WIDTH - self.rect.width: 
            self.rect.x = k.DISPLAY_WIDTH - self.rect.width
        else:
            self.rect.x += self.vel_x
    
    def move_vertical(self):
        if self.rect.y + self.vel_y < 0:
            self.rect.y = 0
        elif self.rect.y + self.vel_y > k.DISPLAY_HEIGHT - self.rect.height: 
            self.rect.y = k.DISPLAY_HEIGHT - self.rect.height
        else:
            self.rect.y += self.vel_y

    def checkBullets(self):
        for bullet in self.bullets:
            if bullet.rect.y <= -10:
                self.bullets.remove(bullet)

    def update(self):
        self.bullets.update()
        self.move_horizontal()
        self.checkBullets()

        if self.isShooting:
            if self.shootingRate%5 == 0:
                self.shoot()
                self.shootingRate = 15

    
        self.shootingRate -=1
        
            
        #print(f'x:{self.rect.x} y:{self.rect.y}')