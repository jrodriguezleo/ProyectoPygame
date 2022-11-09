import pygame as pg
import constants as k
import random as rn

class Arkey(pg.sprite.Sprite):
    def __init__(self):
        super(Arkey,self).__init__()

        self.image = pg.image.load('Enemies\\arkey_sprite.png').convert_alpha()
        scaleFactor = 3
        self.image = pg.transform.scale(self.image, (self.image.get_width()*scaleFactor,self.image.get_height()*scaleFactor))
        self.rect = self.image.get_rect()

        self.rect.x = rn.randint(0, k.DISPLAY_WIDTH- self.rect.width)
        self.rect.y = -self.rect.height

        self.vel_x = 0
        self.vel_y = 15

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y