# 12.4 Rakieta. Utwórz grę rozpoczynającą się od wyświetlenia rakiety na środku ekranu. Pozwól graczowi na poruszanie rakietą w górę, w dół, w lewo i prawo za pomoca klawiszy kursora.

# 12.2 Postać w grze. Wyszukaj obraz przedstawiający postać w grze oraz skonwertuj ten obraz na format rastrowy. Utwórz klase wyświetlającą postać na środku ekranu.


import pygame
import sys

from rocket import Rocket

class ShowRocket:
    """Klasa przeznaczona do wyświetlenia rakiety."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("Rocket")
        self.bg_color = (230, 230, 230)
        self.rocket = Rocket(self)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    rocket = ShowRocket()
    rocket.run_game()
