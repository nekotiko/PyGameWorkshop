from workshop.elements.bricks import RedBrick, SolidPlatform, Pipe
from workshop.elements.enemies import Goomba
from workshop.elements.scenario import ScenarioItem, ScenarioWithImage
from workshop.utils.sprite_loader import get_hill

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

        self.world_shift = 0
        #self.setup()

        self.physics_info = {'play_time': 0, 'seconds': 0, 'current_time': 0}

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.animation_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BACKGROUND_BLUE, None)

        # Draw all the sprite lists that we have
        self.scenario_list.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.animation_list.draw(screen)

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

    def add_point(self, points, rect=None, display=True):
        pass

    def setup(self):
        new_width = SCREEN_WIDTH * 10
        for x in xrange(0, new_width , BLOCK_SIZE):
            self.platform_list.add(SolidPlatform(x, SCREEN_HEIGHT - BLOCK_SIZE))

        for i in xrange(0, 100):
            x = random.randint(0, new_width)
            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE * 2)
            self.platform_list.add(RedBrick(x, y))

        for i in xrange(0, 100):
            x = random.randint(0, new_width)
            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE * 2)
            self.enemy_list.add(Goomba(x, y, level=self))

        for i in xrange(0, 20):
            x = random.randint(0, new_width)
            y = (SCREEN_HEIGHT - BLOCK_SIZE * 2)
            self.add_platform(Pipe(x, y, random.randint(1,6)))

        for i in xrange(0, 40):
            x = random.randint(0, new_width)
            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE * 2)
            self.add_scenario(ScenarioItem(x, y, 'cloud_1'))

            size = random.randint(1,2)
            multi = 4 if size == SCENARIO_BIG_HILL else 3
            x = random.randint(0, new_width)
            y = (SCREEN_HEIGHT - BLOCK_SIZE * multi)

            self.add_scenario(ScenarioWithImage(x, y, get_hill(size)))