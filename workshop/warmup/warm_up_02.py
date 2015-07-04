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

coin = pygame.image.load("../assets/coin.png")
coin_rect = coin.get_rect()
coin = pygame.transform.scale(coin,
                              (int(coin_rect.width * SIZE_MULTIPLIER),
                              int(coin_rect.height * SIZE_MULTIPLIER)))
mario = pygame.image.load("../assets/mario.png")
mariorect = mario.get_rect()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    m_pos = pygame.mouse.get_pos()

    mariorect.left, mariorect.top = m_pos

    mario = pygame.transform.scale(mario,
                                   (int(mariorect.width * SIZE_MULTIPLIER),
                                    int(mariorect.height * SIZE_MULTIPLIER)))
    screen.fill(black)

    for x in xrange(40, width - 40, 40):
        for y in xrange(40, height - 40, 40):
            screen.blit(coin, (x, y))

    screen.blit(mario, mariorect)
    pygame.display.flip()