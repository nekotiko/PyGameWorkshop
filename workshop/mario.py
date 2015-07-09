

__author__ = 'bakeneko'

import pygame
from pygame.sprite import Sprite
from workshop.utils.constants import *

SIZE_MULTIPLIER = 2.5

class Mario(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        mario = pygame.image.load("assets/mario.png")
        mario_rect = mario.get_rect()
        self.image = pygame.transform.scale(mario,
                                   (int(mario_rect.width * SIZE_MULTIPLIER),
                                    int(mario_rect.height * SIZE_MULTIPLIER)))
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.gravity = 0
        self.level = None
        self.state = MARIO_STATE_NORMAL


    def update(self):

        self.calc_grav()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right



        if self.rect.x < 0:
            self.rect.x = 0


        # Move up/down
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            #stop our vertical movements
            self.change_y = 0

        self.change_x = 0

        enemies_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in enemies_hit_list:
            if enemy.state != FIEND_JUMPED_ON and \
                (enemy.rect.collidepoint(self.rect.midbottom) or \
                enemy.rect.collidepoint(self.rect.bottomright) or \
                enemy.rect.collidepoint(self.rect.bottomleft)) : #We kill it!

                self.change_y = -15
                enemy.jumped_on()


    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            if self.change_y < 10: #This is our max falling speed
                self.change_y += self.gravity


    def go_left(self):
        self.change_x = -10

    def go_right(self):
        self.change_x = 10

    def go_up(self):
        self.change_y = -10

