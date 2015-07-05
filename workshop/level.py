from workshop.elements.bricks import RedBrick, SolidPlatform

__author__ = 'bakeneko'

import pygame

from utils.constants import *
import random

class Level(object):

    def __init__(self, player):
        self.platform_list = None
        self.player = player

        self.platform_list = pygame.sprite.Group()
        self.setup()

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLACK, None)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def setup(self):
        for x in xrange(0, SCREEN_WIDTH, BLOCK_SIZE):
            self.platform_list.add(SolidPlatform(x, SCREEN_HEIGHT - BLOCK_SIZE))

        for i in xrange(0, 10):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)
            self.platform_list.add(RedBrick(x, y))