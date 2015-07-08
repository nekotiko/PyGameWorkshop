__author__ = 'bakeneko'

from workshop.utils.constants import BLOCK_SIZE, SCENARIO_BIG_HILL
from workshop.utils.sprite_loader import IMAGE_SLIDER, get_hill, get_pole
from pygame.sprite import Sprite


class ScenarioItem(Sprite):

    def __init__(self, x, y, image_name):
        Sprite.__init__(self)
        self.image = IMAGE_SLIDER.get_image(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ScenarioWithImage(Sprite):

    def __init__(self, x, y, image):
        Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(bottomleft=(x-BLOCK_SIZE, y))
        self.rect.y = y

#===Activity 10

class ScenarioCastle(Sprite):

    def __init__(self, x, y, image ):
        Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(bottomleft=(x+32,y+32))


class Hill(Sprite):

    def __init__(self, x, y, size=SCENARIO_BIG_HILL):
        Sprite.__init__(self)
        self.image = get_hill(size)
        self.rect = self.image.get_rect(bottomleft=(x, y+ 32))


class Pole(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = get_pole()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - BLOCK_SIZE * 9