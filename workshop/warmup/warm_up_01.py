__author__ = 'bakeneko'


__author__ = 'bakeneko'

import pygame
import sys

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

SIZE_MULTIPLIER = 2.5
pos = [1, 1]

screen = pygame.display.set_mode(size)

logo = pygame.image.load("../assets/mario.png")
logorect = logo.get_rect()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass



    screen.fill(black)
    screen.blit(logo, logorect)
    pygame.display.flip()