import pygame as pg
import random as rn
import constants as k
from Background.star import Star

class BG(pg.sprite.Sprite):
    def __init__(self):
        super(BG,self).__init__()
        self.image = pg.Surface(k.DISPLAY_SIZE)
        self.color = (0,0,20)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.stars = pg.sprite.Group()
        self.timer = rn.randint(1,15)

    def checkStars(self):
        for star in self.stars:
            if star.rect.y > k.DISPLAY_HEIGHT +10:
                self.stars.remove(star)

    def drawStar(self):
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = rn.randint(1,10)

        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1

        self.stars.update()


    def update(self):
        self.drawStar()
        self.checkStars()
        #print(f'timer {self.timer}')

