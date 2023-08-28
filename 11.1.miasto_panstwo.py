# 11.1 Miasto, państwo. Przygotuj funkcję akceptującą dwa parametry: nazwy miasta i państwa. Utwórz plik do przetestowania przygotowanej funkcji.
# Uwaga! Aby plik działał, zalecana jest zmiana jego nazwy na 'test_cities'. Obecna nazwa generuje błąd, ale została użyta, aby ułatwić nawigację po programach.

import unittest
from city_functions import get_city_country

class CitiesCountryTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions.py'"""

    def test_city_country(self):
        """Czy dane w postaci 'Santiago, Chile' są obsługiwane prawidłowo?"""

        output = get_city_country('santiago', 'chile')
        self.assertEqual(output, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()