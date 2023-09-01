# 12.1 Niebieskie niebo. Utwórz okno Pygame wraz z tłem w kolorze niebieskim.

import pygame
import sys

class BlueScreen:
    """Klasa przeznaczona do wyświetlenia niebieskiego ekranu."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("Niebieskie niebo")
        self.bg_color = (200, 230, 250)

    def run_game(self):
        while True:
            #Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            #Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    bs = BlueScreen()
    bs.run_game()

