import sys


import pygame


class AlienInvasion:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((500, 500))
		pygame.display.set_caption('Alien Invasion')

		self.bg_color = (0, 10 , 0)

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit

			self.screen.fill(self.bg_color)

			pygame.display.flip()
			

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()


class Settings:
	pass








class Ship:

	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygamme.image.load('/ship.bmg')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		self.screen.blit(self.image, self.rect)





