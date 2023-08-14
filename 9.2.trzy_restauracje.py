# 9.2 Trzy restauracje. Pracę rozpocznij od klasy opracowanej w ćwiczeniu 9.1. Utwórz trzy różne egzemplarze na podstawie tej klasy.

class Restaurant():
    """Tworzy egzemplarz restauracji."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicjalizacja atrybutów restaurant_name i cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Wyświetla dwa fragmenty informacji o restauracji."""
        print(f"Restauracja nazywa się {self.restaurant_name}.")
        print(f"Jest to restauracja {self.cuisine_type}.")

    def open_restaurant(self):
        """Wyświetla informacje o godzinach pracy restauracji."""
        print(f"Dzisiaj restauracja jest otwarta w godzinach 8:00 - 21:00.")

restaurant_1 = Restaurant('Bon Yun Bi', 'koreańska')
restaurant_2 = Restaurant('Domowe obiady', 'polska')
restaurant_3 = Restaurant('Croissant', 'francuska')

restaurant_1.describe_restaurant()
print("\n")
restaurant_2.describe_restaurant()
print("\n")
restaurant_3.describe_restaurant()