# 11.2 Populacja. Zmodyfikuj przygotowaną wcześniej funkcję, aby wymagała trzeciego argumentu - population.
# Uwaga! Aby plik działał, zalecana jest zmiana jego nazwy na 'test_cities'. Obecna nazwa generuje błąd, ale została użyta, aby ułatwić nawigację po programach.

import unittest
from city_functions import get_city_country

class CityCountryPopulationTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions.py'"""

    def test_city_country_population(self):
        output = get_city_country('santiago', 'chile', 5_000_000)
        self.assertEqual(output, 'Santiago, Chile - populacja 5000000')

if __name__ == '__main__':
    unittest.main()