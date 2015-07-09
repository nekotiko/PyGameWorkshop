from workshop.utils.sprite_loader import IMAGE_SLIDER

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
        self.__anti_gravity = False
        self.__cutjump = False

        self.jump_physics = {'vel':0, 'antigravity': 0, 'gravity': PY_JUMP_Y_FALLING_GRAVITY_1}


    def update(self):

        self.calc_grav()


        if self.state == MARIO_STATE_JUMPING:
            self.image = IMAGE_SLIDER.get_mario("small_jumping")

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
                if self.state == MARIO_STATE_JUMPING:
                    self.state = MARIO_STATE_NORMAL
                    self.__cutjump = False

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                self.__anti_gravity = False
                self.__cutjump = True


            # Stop our vertical movement
            self.gravity = 0
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
            seconds = self.level.physics_info['seconds']
            jump_factor = 0

            if self.state == MARIO_STATE_JUMPING and not self.__cutjump:

                if self.__anti_gravity:
                    self.gravity += self.jump_physics['antigravity'] * seconds
                else:
                    self.gravity += self.jump_physics['gravity'] * seconds

                jump_factor = - self.jump_physics['vel'] * seconds

            else:
                self.gravity += self.jump_physics['gravity'] * seconds


            if self.gravity > PY_JUMP_Y_MAX_FALLING_ACC:
                self.gravity = PY_JUMP_Y_MAX_FALLING_RST * seconds

            self.change_y = jump_factor + self.gravity



        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.change_y = 0
            self.gravity = 0


    def go_left(self):
        self.change_x = -10

    def go_right(self):
        self.change_x = 10

    def jump(self):
        """ Called when user hits 'jump' button. """


        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

         # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            seconds =  self.level.physics_info['seconds']
            self.state = MARIO_STATE_JUMPING
            #Define constant Values
            self.jump_physics['vel'] = PY_JUMP_Y_VELOCITY_1
            self.jump_physics['antigravity'] = PY_JUMP_Y_HOLDING_GRAVITY_1
            self.jump_physics['gravity'] = PY_JUMP_Y_FALLING_GRAVITY_1

            self.change_y = -self.jump_physics['vel'] * seconds
            self.__anti_gravity = True
            self.gravity = self.jump_physics['antigravity'] * seconds

    def stop_antigravity(self):
        self.__anti_gravity = False