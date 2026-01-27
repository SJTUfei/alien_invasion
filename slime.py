import pygame

class Slime:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the slime image and get its rect.
        self.image = pygame.image.load('images/slime.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the slime at its current position."""
        self.screen.blit(self.image, self.rect)