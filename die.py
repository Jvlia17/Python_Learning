from random import randint

class Die():
    """Klasa do zaprezentowania kości do gry."""

    def __init__(self, num_sides=6):
        """Inicjalizacja parametrów."""
        self.num_sides = num_sides

    def roll(self):
        """Symulacja rzutukością."""
        return randint(1, self.num_sides)