from workshop.elements.animations import DyingMario

__author__ = 'bakeneko'

import pygame
from pygame.sprite import Sprite
from workshop.utils.constants import *
from workshop.utils.sprite_loader import IMAGE_SLIDER

SIZE_MULTIPLIER = 2.5

class Mario(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self.change_x = 0
        self.change_y = 0
        self.gravity = 0
        self.level = None
        self.state = MARIO_STATE_NORMAL
        self.__anti_gravity = False
        self.__cutjump = False

        self.jump_physics = {'vel':0, 'antigravity': 0, 'gravity': PY_JUMP_Y_FALLING_GRAVITY_1}

        self.__max_vel = PY_MAX_MARIO_WALK_VEL
        self.__speed_acc = PY_MAX_WALK_ACC
        self.__running = False

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []


        # What direction is the player facing?
        self.direction = RIGHT
        for index in xrange(5):
            #print index
            mario_image = IMAGE_SLIDER.get_mario('small_walk_{}'.format(index))
            self.walking_frames_r.append(mario_image)
            rotated = pygame.transform.flip(mario_image, True, False)
            self.walking_frames_l.append(rotated)

        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.speed = 0


    def update(self):

        self.calc_grav()

        pos = self.rect.x + self.level.world_shift

        if self.state == MARIO_STATE_NORMAL:
            if self.change_x:
                frame = int(pos % 30 / 10) + 1
                if self.direction == RIGHT:
                    self.image = self.walking_frames_r[frame]
                else:
                    self.image = self.walking_frames_l[frame]
            else:
                if self.direction == RIGHT:
                    self.image = self.walking_frames_r[0]
                else:
                    self.image = self.walking_frames_l[0]

        elif self.state == MARIO_STATE_JUMPING:
            self.image = IMAGE_SLIDER.get_mario("small_jumping")

        print(self.rect.x)
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



        enemies_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in enemies_hit_list:
            if enemy.state != FIEND_JUMPED_ON and \
                (enemy.rect.collidepoint(self.rect.midbottom) or \
                enemy.rect.collidepoint(self.rect.bottomright) or \
                enemy.rect.collidepoint(self.rect.bottomleft)) : #We kill it!

                self.change_y = -15
                enemy.jumped_on()
            else:
                if enemy.state != FIEND_JUMPED_ON:
                    self.kill()
                    self.level.add_animation(DyingMario(self.rect.x, self.rect.y, self.level))


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
        """ Called when the user hits the right arrow. """
        if self.change_x:
            self.speed += self.__speed_acc
            if self.speed > self.__max_vel:
                self.speed = self.__max_vel

        self.change_x = -(PY_MIN_MARIO_WALK_VEL + self.speed) * self.level.physics_info['seconds']
        self.direction = LEFT

    def go_right(self):
        """ Called when the user hits the right arrow. """
        if self.change_x:
            self.speed += self.__speed_acc
            if self.speed > self.__max_vel:
                self.speed = self.__max_vel

        self.change_x = (PY_MIN_MARIO_WALK_VEL + self.speed) * self.level.physics_info['seconds']
        self.direction = RIGHT

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

    def stop(self):
        """ Called when the user lets off the keyboard. """
        if self.change_x:
            self.speed -= self.__speed_acc
            self.change_x = (PY_MIN_MARIO_WALK_VEL + self.speed) * self.level.physics_info['seconds']
            self.change_x = self.change_x * self.direction
            if self.change_x * self.direction < 0:
                self.change_x = 0
                self.speed = 0




