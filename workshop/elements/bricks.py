import pygame

__author__ = 'bakeneko'


from pygame.sprite import Sprite
from workshop.utils.sprite_loader import IMAGE_SLIDER, get_pipe
from workshop.utils.constants import *



class SolidPlatform(Sprite):

    def __init__(self, x, y, name='red_floor'):
        Sprite.__init__(self)
        self.image = IMAGE_SLIDER.get_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pipe(Sprite):

    def __init__(self, x, y, size=1):
        Sprite.__init__(self)
        self.image = get_pipe(size)
        self.rect = self.image.get_rect(bottomleft=(x,y+BLOCK_SIZE))
        self.mask = pygame.mask.from_surface(self.image)


class RedBrick(Sprite):

    """Bricks that can be destroyed"""
    def __init__(self, x, y, setup_frames=None, level=None, contents=None, powerup_group=None, name='brick'):
        """Initialize the object"""

        #self.sprite_sheet = setup.GFX['tile_set']
        Sprite.__init__(self)
        self.frames = []
        self.frame_index = 0
        self.opened_frame = None

        if setup_frames:
            setup_frames()
        else:
            self.setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bumped_up = False
        self.rest_height = y
        self.state = RESTING
        self.change_y = 0
        self.gravity = 1.2
        self.name = name
        self.contents = contents
        self.setup_contents()
        self.group = powerup_group
        self.powerup_in_box = True
        self.level = None

    def setup_frames(self):
        """Set the frames to a list"""
        self.frames.append(IMAGE_SLIDER.get_image('red_brick'))
        self.frames.append(IMAGE_SLIDER.get_image('empty_brick'))

    def setup_contents(self):
        """Put 6 coins in contents if needed"""
        if self.contents == '6coins':
            self.coin_total = 6
        else:
            self.coin_total = 0

    def update(self):
        """Updates the brick"""
        self.handle_states()

    def handle_states(self):
        """Determines brick behavior based on state"""
        if self.state == RESTING:
            self.resting()
        elif self.state == BUMPED:
            self.bumped()
        elif self.state == OPENED:
            self.opened()

    def resting(self):
        """State when not moving"""
        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state == OPENED

    def bumped(self):
        """Action during a BUMPED state"""
        self.rect.y += self.change_y
        self.change_y += self.gravity

        if self.rect.y >= (self.rest_height + 5):
            self.rect.y = self.rest_height
            if self.contents == 'star':
                self.state = OPENED
            elif self.contents == '6coins':
                if self.coin_total == 0:
                    self.state = OPENED
                else:
                    self.state = RESTING
            else:
                self.state = RESTING


    def start_bump(self):
        """Transitions brick into BUMPED state"""
        if self.state == OPENED:
            return

        self.change_y = -6

        if self.contents == '6coins':


            if self.coin_total > 0:

                self.coin_total -= 1
                if self.coin_total == 0:
                    self.frame_index = 0
                    self.frames = self.opened_frame
                    self.image = self.frames[self.frame_index]

        elif self.contents == 'star':

            self.frame_index = 0
            self.frames = self.opened_frame
            self.image = self.frames[self.frame_index]

        self.state = BUMPED


    def opened(self):
        """Action during OPENED state"""
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        if self.contents == 'star' and self.powerup_in_box:

            self.powerup_in_box = False





class QuestionBox(RedBrick):

    def __init__(self, x, y, level, contents='6coins'):

       RedBrick.__init__(self, x, y, self.setup_frames, contents)

       self.frame_index = 0
       self.level = level
       self.image = self.frames[self.frame_index]
       self.opened_frame = [IMAGE_SLIDER.get_image('question_mark_3')]
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.coin_total = 1
       self.current_time = 0

    def setup_frames(self):
       """Set the frames to a list"""
       for num in xrange(2, -1, -1):
           self.frames.append(IMAGE_SLIDER.get_image('question_mark_{}'.format(num)))
       for num in xrange(0, 3):
           self.frames.append(IMAGE_SLIDER.get_image('question_mark_{}'.format(num)))

    def update(self):

       """Determines brick behavior based on state"""
       if self.state == RESTING:
           self.current_time += 5 * self.level.physics_info['seconds']
           if self.current_time > 5:
               self.current_time = 0
           self.frame_index = int(self.current_time)
           self.image = self.frames[self.frame_index]
           self.resting()
       elif self.state == BUMPED:

           self.bumped()
       elif self.state == OPENED:
           self.opened()

