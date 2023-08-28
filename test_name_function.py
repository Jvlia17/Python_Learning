import unittest
from name_function import get_formatted_name # import funkcji do przetestowania

# zaliczenie testu -> prawidłowe działanie funkcji
# niezaliczenie testu -> istnienie błędu w nowo utworzonym kodzie

class NamesTestCase(unittest.TestCase): # klasa zawierająca serię testów jednostkowych
    """Testy dla programu name_function.py"""

    def test_first_last_name(self): # każda metoda rozpoczynająca się od 'test_' będzie wykonywana automatycznie po uruchomieniu programu
        """Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo?"""

        formatted_name = get_formatted_name('janis', 'joplin') # wywołujemy funkcję get_formatted_name i jej wynik zapisujemy w zmiennej
        self.assertEqual(formatted_name, 'Janis Joplin') # Metoda, którą sprawdzamy czy otrzymany wynik równa się oczekiwanemu.

    def test_first_last_middle_name(self): # ważne! Nazwa musi rozpoczynac się od 'test_'.
        """Czy dane w postaci 'Wolfgang Amadeus Mozart' są obsługiwane prawidłowo?"""

        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__': # Jeśli program został uruchomiony jako program główny -> __name__ = __main__
    unittest.main()