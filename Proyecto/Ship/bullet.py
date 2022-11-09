import pygame as pg
import constants as k

class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        
        self.size = (5, 15)
        self.image = pg.Surface(self.size)
        self.color = (250,180,10)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = -10
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y