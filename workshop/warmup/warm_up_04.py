

__author__ = 'bakeneko'

from workshop.mario import Mario
from workshop.elements.bricks import RedBrick
from pygame.sprite import Sprite
import pygame
import sys

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

SIZE_MULTIPLIER = 2.5
SCORE = [0]
pos = [1, 1]

screen = pygame.display.set_mode(size)

class Coin(Sprite):

   coin = pygame.image.load("../assets/coin.png")
   coin = pygame.transform.scale(coin,
                                  (int(coin.get_rect().width * SIZE_MULTIPLIER),
                                   int(coin.get_rect().height * SIZE_MULTIPLIER)))
   sound = pygame.mixer.Sound("../assets/sound/coin.ogg")

   def __init__(self, x, y):
       Sprite.__init__(self)
       self.image = Coin.coin
       self.rect = self.image.get_rect()
       self.rect.left = x
       self.rect.top = y

   def kill(self):
       Coin.sound.play()
       Sprite.kill(self)
       SCORE[0] += 1000
       print(SCORE)

bricks = pygame.sprite.Group()


bricks.add(RedBrick(40, 40))
bricks.add(RedBrick(80, 40))


mario = Mario(bricks)
player = pygame.sprite.Group()
player.add(mario)


items = pygame.sprite.Group()

for x in xrange(120, width - 40, 40):
    for y in xrange(120, height - 40, 40):
        items.add(Coin(x, y))



all_sprites = pygame.sprite.Group()
all_sprites.add(items)
all_sprites.add(mario)

all_sprites.add(bricks)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario.go_left()
    if keys[pygame.K_RIGHT]:
        mario.go_right()
    if keys[pygame.K_UP]:
        mario.go_up()
    if keys[pygame.K_DOWN]:
        mario.go_down()

    pygame.sprite.spritecollide(mario, items, True)

    all_sprites.update()

    screen.fill(black)

    all_sprites.draw(screen)

    pygame.display.flip()