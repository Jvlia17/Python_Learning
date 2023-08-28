# Najpopularniejsze metody asercji:
# assertEqual() -> czy dwie wartości są sobie równe
# assertNotEqual() -> czy dwie wartości NIE SĄ sobie równe
# assertTrue() -> czy x przyjmuje wartość True
# assertFalse() -> czy x przyjmuje wartość False
# assertIn() -> czy element jest na liście
# assertNotIn() -> czy elementu NIE MA na liście

# 11.3 Pracownik. Przygotuj klasę o nazwie Employee. Metoda __init__() powinna pobierać imię, nazwisko i roczne wynagrodzenie, a następnie zapisywać te informacje w postaci atrybutów.
# Uwaga! Aby plik działał, zalecana jest zmiana jego nazwy na 'test_employee'. Obecna nazwa generuje błąd, ale została użyta, aby ułatwić nawigację po programach.

import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Testy dla klasy Employee."""

    def setUp(self):
        """Utworzenie pracownika i różnych podwyżek."""
        self.my_employee = Employee('Julia', 'Rzepka', 0)

    def test_give_default_raise(self):
        """Sprawdzenie, czy program poprawnie daje domyślną podwyżkę."""
        self.my_employee.give_raise()
        current_salary = self.my_employee.salary
        self.assertEqual(current_salary, 5000)

    def test_give_custom_raise(self):
        """Sprawdzenie, czy program poprawnie daje customową podwyżkę."""
        self.my_employee.give_raise(6000)
        current_salary = self.my_employee.salary
        self.assertEqual(current_salary, 6000)

if __name__ == '__main__':
    unittest.main()