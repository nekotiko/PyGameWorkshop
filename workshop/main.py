from workshop import level

__author__ = 'bakeneko'

import pygame
from workshop.mario import Mario
from workshop.utils.constants import *


def main():
    """ Main Program """
    pygame.init()

    clock = pygame.time.Clock()

    # Set the height and width of the screen

    screen = pygame.display.set_mode(SIZE, pygame.DOUBLEBUF, 32)

    pygame.display.set_caption("Super Mario Bros!")

    # Create the player
    mario = Mario()

    current_level = level.Level(mario)

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(mario)

    mario.level = current_level

    done = False

    while not done:
        milliseconds =  clock.tick(FPS)

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mario.go_left()
        if keys[pygame.K_RIGHT]:
            mario.go_right()
        if keys[pygame.K_UP]:
            mario.go_up()
        if keys[pygame.K_DOWN]:
            mario.go_down()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()