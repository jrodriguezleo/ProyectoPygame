# from dis import dis
# from sys import displayhook
# from tkinter import E
from dis import dis
import pygame
import constants as k
from Ship.ship import Ship
from Background.Background import BG
from Enemies.enemies_spawner import EnemySpawner

#initialising pygame
pygame.init()

#defining size of game window
display = pygame.display.set_mode((k.DISPLAY_WIDTH,k.DISPLAY_HEIGHT)) 

#define the title of the window
pygame.display.set_caption("Galaga")

#set a cap in the fps / Hz of everything
fps = 30
clock = pygame.time.Clock()

#Intialize some objects
player = Ship()
enemySpawner = EnemySpawner()

#Agroup all the sprites to update them at the same time
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

#intialize the background
bg = BG()
bg_sprite_group = pygame.sprite.Group()
bg_sprite_group.add(bg)

black = (0,0,0)

running = True
while running:
    #Ticks 
    clock.tick(fps)

    #Handle events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        #check for pressing keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.vel_x = -player.speed
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.vel_x = player.speed
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.vel_y = -player.speed
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.vel_y = player.speed

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.isShooting = True

        
        #check for realising keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.vel_x = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.vel_x = 0
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.vel_y = 0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.vel_y = 0
                
        if event.type == pygame. KEYUP:
            if event.key == pygame.K_SPACE:
                player.isShooting = False
    
    #Update all the objects
    bg_sprite_group.update()
    sprite_group.update()
    enemySpawner.update()
    


    #Render the display
    display.fill(black)
    bg_sprite_group.draw(display)
    enemySpawner.enemy_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    pygame.display.update()