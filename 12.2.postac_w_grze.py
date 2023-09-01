# 12.2 Postać w grze. Wyszukaj obraz przedstawiający postać w grze oraz skonwertuj ten obraz na format rastrowy. Utwórz klase wyświetlającą postać na środku ekranu.


import pygame
import sys

from spiderman import Spiderman

class Superhero:
    """Klasa przeznaczona do wyświetlenia niebieskiego ekranu."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("Spider-man")
        self.bg_color = (250, 100, 100)
        self.hero = Spiderman(self)

    def run_game(self):
        while True:
            #Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.hero.blitme()
            #Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    hero = Superhero()
    hero.run_game()
