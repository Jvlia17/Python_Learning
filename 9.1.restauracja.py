'''
class Dog(): # z wielkiej litery
    """Prosta próba modelowania psa."""
    def __init__(self, name, age):
        """Inicjalizacja atrybutów name i age."""
        # Metoda __innit__ jest wywołana przez Pythona automatycznie podczas tworzenia egzemplarza klasy.
        # atrybut self musi znajdować się jako pierwszy i jest odwołaniem do danego egzemplarza (obiektu).
        # jeśli zmienna ma prefiks self, to jest dostępna dla każdej metody w klasie.
        # Metoda -> inaczej funkcja będąca częścią klasy.
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia."""
        print(f"{self.name.title()} teraz siedzi.")

    def roll_over(self):
        """Symulacja, że pies kładzie się na plecach po otrzymaniu polecenia."""
        print(f"{self.name.title()} teraz położył się na plecy!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)

print(f"Mój pies ma na imię {my_dog.name.title()}.")
print(f"Mój pies ma {my_dog.age} lat.")
my_dog.sit()

print(f"\nTwój pies ma na imię {your_dog.name.title()}.")
print(f"Twój pies ma {your_dog.age} lat.")
your_dog.roll_over()
'''

# 9.1 Restauracja. Przygotuj klasę o nazwie Restaurant.

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

restaurant = Restaurant('Bon Yun Bi', 'koreańska')

print(f"Restauracja polecana na dzisiaj to {restaurant.restaurant_name}!")
print(f"Jest to restauracja {restaurant.cuisine_type}.\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()