import pygame

__author__ = 'bakeneko'


from pygame.sprite import Sprite
from workshop.utils.sprite_loader import IMAGE_SLIDER, get_pipe
from workshop.utils.constants import *

class RedBrick(Sprite):

    def __init__(self, x, y, image='red_brick'):
        Sprite.__init__(self)
        self.image = IMAGE_SLIDER.get_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class SolidPlatform(RedBrick):

    def __init__(self, x, y):
        RedBrick.__init__(self, x, y, 'solid_brick')


class Pipe(Sprite):

    def __init__(self, x, y, size=1):
        Sprite.__init__(self)
        self.image = get_pipe(size)
        self.rect = self.image.get_rect(bottomleft=(x,y+BLOCK_SIZE))
        self.mask = pygame.mask.from_surface(self.image)