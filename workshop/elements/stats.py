from workshop.utils.loader import get_font
from workshop.utils.sprite_loader import IMAGE_SLIDER

__author__ = 'bakeneko'




class Stats(object):

    def __init__(self, level, time=400 ):
        self.font = get_font(16)
        self.world = ' 1-1 '
        self.worltime  = 0
        self.lives = 3
        self.score = 0
        self.coins = 0
        self.time = 400
        self.x = IMAGE_SLIDER.get_item('score_x', 1.5)
