__author__ = 'bakeneko'

from workshop.utils.constants import BLOCK_SIZE
from workshop.utils.sprite_loader import IMAGE_SLIDER
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

