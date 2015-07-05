
__author__ = 'bakeneko'


from pygame.sprite import Sprite
from workshop.utils.sprite_loader import IMAGE_SLIDER

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