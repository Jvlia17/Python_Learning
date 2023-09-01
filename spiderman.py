import pygame

class Spiderman:
    """Klasa przeznaczona do zarządzania Spider-manem"""

    def __init__(self, hero):
        self.screen = hero.screen
        self.screen_rect = hero.screen.get_rect()

        self.image = pygame.image.load('images/spiderman.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)