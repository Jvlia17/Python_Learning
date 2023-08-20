'''
class Car():
    """Prosta próba zaprezentowania samochodu."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100 # przypisanie atrybutowi wartości domyślnej

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu."""
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu samochodu."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną wartość."""
        self.odometer_reading += kilometers

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

 # Pierwszy sposób zmiany atrybutu -> bezpośrednia modyfikacja atrybutu
my_new_car.odometer_reading = 0
my_new_car.read_odometer()

# Drugi sposób modyfikacji atrybutu -> za pomocą metody
my_new_car.update_odometer(23_000)
my_new_car.read_odometer()

# Trzeci sposób zmiany atrybutu -> inkrementacja wartości atrybutu za pomocą metody
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
'''

# 9.4 Liczba obsłużonych. Pracę rozpocznij od programu utworzonego w ćwiczeniu 9.1. Dodaj atrybut o nazwie number_served o wartości domyślnej 0.

class Restaurant():
    """Tworzy egzemplarz restauracji."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicjalizacja atrybutów restaurant_name i cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Wyświetla dwa fragmenty informacji o restauracji."""
        print(f"Restauracja nazywa się {self.restaurant_name}.")
        print(f"Jest to restauracja {self.cuisine_type}.")

    def open_restaurant(self):
        """Wyświetla informacje o godzinach pracy restauracji."""
        print(f"Dzisiaj restauracja jest otwarta w godzinach 8:00 - 21:00.")

    def set_number_served(self, clients):
        """Definiuje liczbę obsłużonych klientów."""
        self.number_served = clients

    def increment_number_served(self, clients):
        """Zwiększa wartość wskazującą na liczbę obsłużonych klientów."""
        self.number_served += clients

restaurant = Restaurant('Bon Yun Bi', 'koreańska')

print(f"Restauracja polecana na dzisiaj to {restaurant.restaurant_name}!")
print(f"Jest to restauracja {restaurant.cuisine_type}.\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Liczba obsłużonych klientów na ten moment to: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Liczba obsłużonych klientów na ten moment to: {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Liczba obsłużonych klientów na ten moment to: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Liczba obsłużonych klientów na ten moment to: {restaurant.number_served}")