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

        self.enemy_list     = pygame.sprite.Group()
        self.brick_list     = pygame.sprite.Group()
        self.scenario_list  = pygame.sprite.Group()
        #Animations are elements that interact with nothing and will be removed soon
        self.animation_list  = pygame.sprite.Group()

        self.world_shift_x = 0
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

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for scenario in self.scenario_list:
            scenario.rect.x += shift_x

        for animation in self.animation_list:
            animation.rect.x += shift_x


    def add_platform(self, platform):
        self.platform_list.add(platform)

    def add_brick(self, brick):
        self.brick_list.add(brick)
        self.add_platform(brick)

    def add_enemy(self, enemy):
        self.enemy_list.add(enemy)

    def add_scenario(self, scenario):
        self.scenario_list.add(scenario)

    def add_animation(self, animation):
        self.animation_list.add(animation)

    def setup(self):
        new_width = SCREEN_WIDTH * 10
        for x in xrange(0, new_width , BLOCK_SIZE):
            self.platform_list.add(SolidPlatform(x, SCREEN_HEIGHT - BLOCK_SIZE))

        for i in xrange(0, 100):
            x = random.randint(0, new_width)
            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE * 2)
            self.platform_list.add(RedBrick(x, y))