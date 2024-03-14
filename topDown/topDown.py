import pygame
from sys import exit
import math
from settings import * 

pygame.init()

#Making window

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("TopDown Shooter")

clock = pygame.time.Clock()

#Loading our images
background = pygame.transform.scale(pygame.image.load("top-down-shooter/background/background.png").convert(), (width, height))

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(fps)