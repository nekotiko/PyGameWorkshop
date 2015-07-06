from workshop.utils.sprite_loader import IMAGE_SLIDER

__author__ = 'bakeneko'



import pygame
from pygame.sprite import Sprite
from workshop.utils.constants import *

class Enemy(Sprite):

    """Base class for all enemies (Goombas, Koopas, etc.)"""
    def __init__(self):
        Sprite.__init__(self)
        self.gravity = 4.5
        self.state = FIEND_WALK
        self.change_x = 0
        self.change_y = 0
        self.current_time = 0

        self.frames = []
        self.frame_index = 0
        self.direction = LEFT





    def setup_enemy(self, x, y, level, direction, name, setup_frames):

        """Sets up various values for enemy"""
        #self.sprite_sheet = setup.GFX['smb_enemies_sheet']

        self.level = level
        self.name = name

        self.direction = direction
        self.image_direction = direction

        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.set_velocity()


    def set_velocity(self):
        """Sets velocity vector based on direction"""
        if self.direction == LEFT:
            self.change_x = -1
        else:
            self.change_x = 1

        #let's flip the direction
        if self.direction != self.image_direction:
            self.image_direction = self.direction

            for index, image in enumerate(self.frames):
                self.frames[index] = pygame.transform.flip(image, True, False)

        self.change_y = 0


    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == FIEND_WALK:
            self.walking()
        elif self.state == FIEND_FALLING:
            self.falling()
        elif self.state == FIEND_JUMPED_ON:
            self.jumped_on()

    def walking(self):

        self.calc_grav()

        """Default state of moving sideways"""
        if self.current_time  > 0.25:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.current_time = 0

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        try:
            enemy_hit_list.remove(self)
        except ValueError: #The is nothing to do we don't exist anymore
            pass

        block_hit_list.extend(enemy_hit_list)

        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.direction = LEFT
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.direction = RIGHT

            self.set_velocity()

        #move up and down.
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # Check if it is falling
        for block in block_hit_list:
        # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            if self.change_y < 150:
                self.change_y += self.gravity

        # See if falling out of the screen
        if self.rect.y >= SCREEN_HEIGHT + self.rect.height  and self.change_y >= 0:
            self.kill()

    def falling(self):
        """For when it falls off a ledge"""
        if self.change_y < 10:
            self.change_y += self.gravity

    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass

    def animation(self):
        """Basic animation, switching between two frames"""
        self.image = self.frames[self.frame_index]

    def update(self):
        """Updates enemy behavior"""
        #We only want enemies to move when we are close
        pos = abs(self.level.world_shift - SCREEN_WIDTH)

        if self.rect.x <= pos:
            self.current_time += self.level.physics_info['seconds']
            self.handle_state()
            self.animation()
            if self.rect.x <= - BLOCK_SIZE * 5: #Too far behind let's get rid of it
                self.kill()
