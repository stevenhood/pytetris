#! /usr/bin/env python

# pytetris
# author	Steven Hood

# Python 2.7.3
# Pygame 1.9.1 (release)

import sys # exit
import random
import pygame
from pygame.sprite import Sprite

pygame.init()
random.seed()

SQUARE_DIMENSIONS = SQUARE_WIDTH, SQUARE_HEIGHT = 30, 30
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT = SQUARE_WIDTH * 10, SQUARE_HEIGHT * 20


class Square(Sprite):
	""" Represents an individual square in a tetromino. """
	def __init__(self, color, position):
		Sprite.__init__(self)
		self.image = pygame.Surface(SQUARE_DIMENSIONS)
		self.image.fill(pygame.Color(color))
		# get sprite bounding box, set initial position
		self.rect = self.image.get_rect()
		self.rect.center = position

	def move(self, x, y):
		self.rect.move_ip(x, y)


def main():
	screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
	pygame.display.set_caption('pytetris')
	background = pygame.Surface(WINDOW_DIMENSIONS)
	background.fill(pygame.Color('black'))
	screen.blit(background, (0, 0))

	def end(): sys.exit(0)
	key_map = {
		pygame.K_ESCAPE: end
	}
	pygame.key.set_repeat(1, 50)

	clock = pygame.time.Clock()
	square = Square('red', (160, 120))
	sprites = pygame.sprite.RenderClear([square])
	running = True

	while running:
		clock.tick(30)
		pygame.display.set_caption('pytetris :: {0:.2f} fps'.format(clock.get_fps()))

		# animate and draw sprites, display screen
		sprites.update()
		sprites.draw(screen)
		pygame.display.flip()

		# draw background over old sprites
		sprites.clear(screen, background)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key in key_map:
				key_map[event.key]()


if __name__ == '__main__':
	main()
