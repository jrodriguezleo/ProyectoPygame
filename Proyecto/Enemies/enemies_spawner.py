import pygame as pg
import constants as k
import random as rn
from Enemies.Arkey import Arkey

class EnemySpawner:
    def __init__(self):
        self.enemy_group = pg.sprite.Group()
        self.spawn_timer = rn.randint(30,120)

    def spawnEnemy(self):
        new_arkey = Arkey()
        self.enemy_group.add(new_arkey)

    def update(self):
        self.enemy_group.update()
        if self.spawn_timer == 0:
            self.spawnEnemy()
            self.spawn_timer = rn.randint(30,120)

        self.spawn_timer -=1
