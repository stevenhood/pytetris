#!/usr/bin/env python

# author	Steven Hood
# date		27/07/2014

# Python 2.7.3
# Pygame 1.9.1 (release)

import pygame, random
from pygame.sprite import Sprite

pygame.init()
random.seed()

WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480


class Ball(Sprite):
	def __init__(self, color, position):
		Sprite.__init__(self)

		# create surface, draw filled circle
		self.image = pygame.Surface([6, 6])
		pygame.draw.circle(self.image, pygame.Color(color), (3, 3), 3)

		# get sprite bounding box, set initial position
		self.rect = self.image.get_rect()
		self.rect.center = position

	def update(self):
		x = random.randint(-3, 3)
		y = random.randint(-3, 3)
		self.rect.move_ip(x, y)


def main():
	screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
	background = pygame.Surface(WINDOW_DIMENSIONS)
	background.fill(pygame.Color("black"))
	screen.blit(background, (0, 0))
	pygame.display.set_caption("WINDOW TITLE")
	clock = pygame.time.Clock()

	ball = Ball("white", (160, 120))
	# list of sprites to render
	sprites = pygame.sprite.RenderClear([ball])
	running = True

	while running:
		clock.tick(30)
		pygame.display.set_caption("WINDOW TITLE - {0:.2f} fps".format(clock.get_fps()))

		# animate and draw sprites, display screen
		sprites.update()
		sprites.draw(screen)
		pygame.display.flip()

		# draw background over old sprites
		sprites.clear(screen, background)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


if __name__ == "__main__":
	main()
