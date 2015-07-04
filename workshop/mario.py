__author__ = 'bakeneko'

import pygame
from pygame.sprite import Sprite

SIZE_MULTIPLIER = 2.5

class Mario(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        mario = pygame.image.load("../assets/mario.png")
        mario_rect = mario.get_rect()
        self.image = pygame.transform.scale(mario,
                                   (int(mario_rect.width * SIZE_MULTIPLIER),
                                    int(mario_rect.height * SIZE_MULTIPLIER)))
        self.rect = self.image.get_rect()

    def update(self):
        m_pos = pygame.mouse.get_pos()
        self.rect.left, self.rect.top = m_pos