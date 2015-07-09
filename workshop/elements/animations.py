from workshop.utils.sprite_loader import IMAGE_SLIDER

__author__ = 'bakeneko'

import pygame
from pygame.sprite import Sprite
from workshop.utils.constants import *

class DyingMario(Sprite):

    def __init__(self, x, y, level):
        # Call the parent's constructor
        Sprite.__init__(self)

        # Set the image the player starts with
        # Set speed vector of player
        self.image = IMAGE_SLIDER.get_mario('dying')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = level
        self.change_y = -PY_JUMP_Y_VELOCITY_1 * self.level.physics_info['seconds']
        self.gravity = 0


    def update(self):
        seconds = self.level.physics_info['seconds']
        self.gravity += PY_JUMP_Y_HOLDING_GRAVITY_1 * seconds
        self.change_y = (-PY_JUMP_Y_VELOCITY_1 * seconds) + self.gravity
        self.rect.y += self.change_y
        if self.rect.y >= SCREEN_HEIGHT + self.rect.height:
            self.kill()


