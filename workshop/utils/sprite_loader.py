__author__ = 'bakeneko'

import pygame
from constants import *

TILE_IMAGE = None
MARIO_IMAGES = None
ENEMY_IMAGES = None
ITEMS_IMAGES = None


#x,y, width, height
SPRITE_DIMENTIONS = {
        'red_floor': (0, 0, 16, 16),

        'red_brick': (16, 0, 16, 16),
        'empty_brick': (432, 0, 16, 16),
        'broken_brick': (68, 20, 8, 8),
        'solid_brick': (0, 16, 16, 16),

        'question_mark_0': (384, 0, 16, 16),
        'question_mark_1': (400, 0, 16, 16),
        'question_mark_2': (416, 0, 16, 16),
        'question_mark_3': (432, 0, 16, 16),#empty

        'mario_small_walk_0' : (178, 32, 12, 16),
        'mario_small_walk_1' : (80, 32, 14, 16),
        'mario_small_walk_2' : (98, 32, 12, 16),
        'mario_small_walk_3' : (114, 32, 12, 16),
        'mario_small_walk_4' : (128, 32, 14, 16),
        'mario_small_jumping': (144, 32, 16, 16),
        'mario_dying': (160, 32, 16, 16),

        'goomba_1': (0, 16, 16, 16),
        'goomba_2': (16,16, 16, 16),
        'goomba_3': (32,16, 16, 16),

        'turtle_1': (96, 8, 16, 24),
        'turtle_2': (112,8, 16, 24),
        'turtle_3': (160,16, 16, 16),

        'cloud_1':    (0,320,45,24),

        'mountain_0': (128,128,16,16),
        'mountain_1': (128,144,16,16),
        'mountain_2': (144,128,16,16),
        'mountain_3': (144,144,16,16),
        'mountain_4': (160,128,16,16),
        'mountain_5': (160,144,16,16),

        'pipe_top': (1, 129, 30, 14),
        'pipe_body': (3, 144, 26, 15),

        'bush_0': (176, 144, 16, 16),
        'bush_1': (192, 144, 16, 16),
        'bush_2': (208, 144, 16, 16),

        'castle_0': (176, 0, 16, 16),
        'castle_1': (176, 16, 16, 16),
        'castle_2': (192, 0, 16, 16),
        'castle_3': (192, 16, 16, 16),
        'castle_4': (208, 16, 16, 16),
        'castle_5': (208, 0, 16, 16),
        'castle_6': (224, 0, 16, 16),

        'collected_coin_0': (5, 112, 10, 14 ),
        'collected_coin_1': (18, 112, 10, 14),
        'collected_coin_2': (36, 112, 10, 15),
        'collected_coin_3': (54, 112, 10, 16),

        'score_coin_0': (0, 160, 6, 8),
        'score_coin_1': (8, 160, 6, 8),
        'score_coin_2': (16, 160, 6, 8),

        'score_x': (40, 160, 8, 8),

        'pole_body': (256, 144, 16, 16),
        'pole_top':  (256, 128, 16, 16),
        'pole_flag': (128,32, 16, 16)

}


class ImageSlider(object):
    """
    This class cuts the sprites sheets
    """

    def __init__(self):
        print "BrickSlider Inited"
        self.images = {}

    def get_item(self, name, multiplier=SIZE_MULTIPLIER):
        image = self._get_image(name, 'assets/item_objects.png', 'items', multiplier)
        return image

    def get_mario(self, name):
        return self._get_image('mario_' + name, 'assets/mario_bros.png', 'mario')

    def get_image(self, name, multiplier=SIZE_MULTIPLIER):
        return self._get_image(name, 'assets/tile_set.png', 'asset', multiplier)


    def get_enemies(self, name):
        image = self._get_image(name, 'assets/enemies.png', 'enemies')
        return image

    def _get_image(self, name, path, type, multiplier=SIZE_MULTIPLIER):
        image = self.images.get(name)
        if not image:
            image = self._cut_image(name, path, type, multiplier)
            self.images[name] = image

        return image

    def _cut_image(self, name, path, type_name, multiplier=SIZE_MULTIPLIER):
        global TILE_IMAGE
        global MARIO_IMAGES
        global ENEMY_IMAGES
        global ITEMS_IMAGES

        if not ITEMS_IMAGES and type_name == 'items':
            ITEMS_IMAGES = ImageSlider.convert(pygame.image.load(path))

        if not TILE_IMAGE and type_name == 'asset':
            TILE_IMAGE = ImageSlider.convert(pygame.image.load(path))

        if not MARIO_IMAGES and type_name == 'mario':
            MARIO_IMAGES = ImageSlider.convert(pygame.image.load(path))

        if not ENEMY_IMAGES and type_name == 'enemies':
            ENEMY_IMAGES = ImageSlider.convert(pygame.image.load(path))

        IMAGE = TILE_IMAGE
        if type_name == 'mario':
            IMAGE = MARIO_IMAGES
        elif type_name == 'enemies':
            IMAGE = ENEMY_IMAGES
        elif type_name == 'items':
            IMAGE = ITEMS_IMAGES

        dimensions = SPRITE_DIMENTIONS[name]
        width, height = dimensions[2:4]

        # Create a new blank image, the SRCALPHA will keep the Alpha information form the orginal PNG
        image = pygame.Surface([width, height], pygame.SRCALPHA, 32)

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(IMAGE, (0, 0), dimensions)
        scale_image = pygame.transform.scale(image,
                                         (int(width * multiplier),
                                          int(height * multiplier)))
        return scale_image

    @staticmethod
    def convert(image):
        if image.get_alpha():
            img = image.convert_alpha()
            return img
        else:
            img = image.convert()
            return img



#Instanciate the Image Slider Object
IMAGE_SLIDER = ImageSlider()

def get_pipe(size=1):
    top = IMAGE_SLIDER.get_image('pipe_top')
    body = IMAGE_SLIDER.get_image('pipe_body')
    b_height = body.get_height()

    height = top.get_height() + (b_height * size)
    width = top.get_width()

    new_pipe = pygame.Surface([width, height], pygame.SRCALPHA, 32)

    new_pipe.blit(top, (0, 0))
    for y in xrange(top.get_height(), b_height * size + 1, b_height):
        new_pipe.blit(body, (4, y))

    return new_pipe
