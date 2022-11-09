import pygame as pg
import random as rn
import constants as k

class Star(pg.sprite.Sprite):
    def __init__(self):
        super(Star,self).__init__()

        self.width = rn.randint(5,10)
        self.heigth = rn.randint(5,10)
        self.size = (self.width,self.heigth)

        self.image = pg.Surface(self.size)
        self.color = (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = rn.randint(0,k.DISPLAY_WIDTH)

        self.vel_x = 0
        self.vel_y = rn.randint(5,25)



    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
