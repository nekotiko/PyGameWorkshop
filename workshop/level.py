__author__ = 'bakeneko'

import pygame

from utils.constants import *

class Level(object):

    def __init__(self, player):
        self.platform_list = None
        self.player = player

        self.platform_list  = pygame.sprite.Group()
        self.setup()

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLACK,  None)


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def setup(self):
        pass