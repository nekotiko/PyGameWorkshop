__author__ = 'bakeneko'
from pygame import Color



#Activity 3

SIZE_MULTIPLIER=2.5

#Activity 05


BLACK = Color('black')
FPS = 60
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

ORIGINAL_BLOCK_SIZE = 16
SIZE_MULTIPLIER = 2
BLOCK_SIZE = ORIGINAL_BLOCK_SIZE * SIZE_MULTIPLIER
GROUND_HEIGHT = SCREEN_HEIGHT - BLOCK_SIZE * 2

#Activity 07

FIEND_WALK, \
FIEND_FALLING, \
FIEND_JUMPED_ON = range(0,3)
LEFT = -1
RIGHT = 1

BACKGROUND_BLUE = (113, 144, 254)


SCENARIO_BIG_HILL = 1
SCENARIO_SMALL_HILL = 2

#===Activity 10 MAP
MAP_QUESTION_BLOCK = (127, 51, 0)
MAP_BRICK          = (0, 74, 127)
MAP_BRICK_HOLDER    = (109, 127, 63)
MAP_SOLID_BLOCK    = (255, 200, 0)
MAP_CLOUD_1        = (87, 0, 127)
MAP_EMPTY          = (254, 254, 255)
MAP_BIG_MOUNTAIN   = (255, 233, 127)
MAP_SMALL_MOUNTAIN = (218, 255, 127)
MAP_SHORT_PIPE     = (148, 171, 91)
MAP_MID_PIPE       = (91, 127, 0)
MAP_TALL_PIPE     = (178, 0, 255)
MAP_COIN          = (255, 255, 0)
MAP_SINGLE_BUSH    =  (177, 220, 255)
MAP_DOUBLE_BUSH    = (127, 255, 142)
MAP_TRIPLE_BUSH    = (127, 0, 55)
MAP_FLAG           = (0, 255, 0)
MAP_SMALL_CASTLE   = (80, 63, 127)
MAP_GOOMBA_1       = (0, 255, 255)
MAP_TURTLE     = (127, 201, 255)
MAP_1UP = (0, 127, 70)



MARIO_STATE_NORMAL = 0
MARIO_STATE_JUMPING = 1

"""
Physics according a complete guide to SMB's Physics engine
the velocities will be expresed in /16 of the previos so
 * 16 Block
 / 1 pixel
 / 16.0 subpixel
 / 16.0 / 16.0 ss-pixel
 / 16.0 / 16.0 / 16.0 sss-pixel

 This numbers are for frame-based movement, we can do time-based movement but it will require convertion
"""
def doc_unit_to_value(num):
    if len(num) != 5:
        raise ValueError('Number can be only a String of 5 digits')

    sum = int(num[0], 16) * 16.0 + \
          int(num[1], 16) + \
          int(num[2], 16) / 16.0 + \
          int(num[3], 16) / 16.0 / 16.0 + \
          int(num[4], 16) / 16.0 / 16.0 / 16.0
    return sum * SIZE_MULTIPLIER

def doc_unit_to_pixels_per_second(num):
    pixels_per_frame = doc_unit_to_value(num)
    return pixels_per_frame * FPS

PY_MAX_MARIO_WALK_VEL = doc_unit_to_pixels_per_second('01900')
PY_MIN_MARIO_WALK_VEL = doc_unit_to_pixels_per_second('00130')
PY_MARIO_WALK_ACC     = doc_unit_to_pixels_per_second('00098')
PY_MARIO_WALK_DEC     = doc_unit_to_pixels_per_second('000D0')
PY_MAX_MARIO_RUN_VEL  = doc_unit_to_pixels_per_second('02900')
PY_MARIO_RUN_ACC  = doc_unit_to_pixels_per_second('000E4')

PY_JUMP_X_VELOCITY_1 = doc_unit_to_pixels_per_second('01000')
PY_JUMP_X_VELOCITY_2 = doc_unit_to_pixels_per_second('024FF')
PY_JUMP_X_VELOCITY_3 = doc_unit_to_pixels_per_second('02500')

PY_JUMP_Y_VELOCITY_1 = doc_unit_to_pixels_per_second('04000')
PY_JUMP_Y_VELOCITY_2 = doc_unit_to_pixels_per_second('04000')
PY_JUMP_Y_VELOCITY_3 = doc_unit_to_pixels_per_second('05000')

PY_JUMP_Y_HOLDING_GRAVITY_1 = doc_unit_to_pixels_per_second('00200')
PY_JUMP_Y_HOLDING_GRAVITY_2 = doc_unit_to_pixels_per_second('001E0')
PY_JUMP_Y_HOLDING_GRAVITY_3 = doc_unit_to_pixels_per_second('00280')

PY_JUMP_Y_FALLING_GRAVITY_1 = doc_unit_to_pixels_per_second('00700')
PY_JUMP_Y_FALLING_GRAVITY_2 = doc_unit_to_pixels_per_second('00600')
PY_JUMP_Y_FALLING_GRAVITY_3 = doc_unit_to_pixels_per_second('00900')

PY_JUMP_Y_MAX_FALLING_ACC = doc_unit_to_pixels_per_second('04800')
PY_JUMP_Y_MAX_FALLING_RST = doc_unit_to_pixels_per_second('04000')

PY_ENEMY_STOMP_Y_SPEED = doc_unit_to_pixels_per_second('04000')

#Non offical
PY_ENEMY_WALK_SPEED    = doc_unit_to_pixels_per_second('08000')


##Deduced PY
PY_MAX_WALK_ACC = PY_MAX_MARIO_WALK_VEL - PY_MIN_MARIO_WALK_VEL


SCREEN_PLAYER_OFFSET = SCREEN_WIDTH / 3 * 2 #2/3 of the screen

#activity
#BRICK STATES

RESTING = 'resting'
BUMPED = 'bumped'

#COIN STATES
OPENED = 'opened'

MUTE = True