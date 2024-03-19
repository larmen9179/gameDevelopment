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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load("top-down-shooter/player/player.png").convert_alpha(), 0, 1.85)
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.speed = PLAYER_SPEED

    def userInput(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed

        if keys[pygame.K_s]:
            self.velocity_y = self.speed

        if keys[pygame.K_a]:
            self.velocity_x = -self.speed

        if keys[pygame.K_d]:
            self.velocity_x = self.speed

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)

    def update(self):
        self.userInput()
        self.move()
player = Player()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.pos)
    player.update()

    pygame.display.update()
    clock.tick(fps)