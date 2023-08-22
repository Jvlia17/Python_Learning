'''
from random import randint, choice

number = randint(1, 6) # Funkcja randint() pobiera dwie liczby i zwraca losowo wybraną liczbę z zakresu tych liczb.
print(number)

players = ['karol', 'mateusz', 'kinga', 'oliwier']
first_up = choice(players) # Funkcja choice() pobiera listę lub krotkę, a następnie zwraca losowo wybrany element.
print(first_up)
'''

# 9.13 Kości do gry. Przygotuj klasę Die z jednym atrybutem o nazwie sides, którego wartością domyślną będzie 6. Utwórz metodę o nazwie roll_die(), wyświetlającą losowo wygenerowaną liczbę z zakresu od 1 do wartości określonej przez liczbę ścianek na kości do gry.
from random import randint


class Die():
    """Klasa do prostego zaprezentowania rzutu kością."""

    def __init__(self):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.sides = 20

    def roll_die(self):
        """Prosta symulacja rzutu kością."""
        print(f"Wykulałeś: {randint(1, self.sides)}")


die = Die()
die.roll_die()
