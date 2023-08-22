"""Zestaw klas przeznaczonych do zaprezentowania samochodu,
zarówno o napędzie tradycyjnym, jak i elektrycznym."""

class Car(): # Klasa Car to u nas klasa nadrzędna. Musi zawsze znajdowac się w bieżącym pliku.
    """Prosta próba zaprezentowania samochodu."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu."""
        print(f"Ten samochód ma przejechane {self.odometer_reading}km.")

    def fill_gas_tank(self):
        """Tankuje samochód."""
        print("Zatankowano samochód!")

    def update_odometer(self, mileage):
        """
        Przypisanie podanej wartościlicznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku próby cofnięcia licznika.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną
        wartość."""
        self.odometer_reading += kilometers


class Battery(): # Nowa klasa, która po nikim nie dziedziczy.
    """Prosta próba modelowania akumulatora samochodu elektrycznego."""

    def __init__(self, battery_size=75): # parametr opcjonalny
        """Inicjalizacja atrybutów akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlanie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.")

    def get_range(self):
        """
        Wyświetla informacje o zasięgu samochodu na podstawie pojemności
        akumulatora.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Zasięg tego samochodu wynosi około {range} km po pełnym naładowaniu akumulatora.")

class ElectricCar(Car): # Klasa nadrzędna w nawiasie klasy potomnej
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """
        Inicjalizacja atrybutów klasy nadrzędnej.
        Następnie inicjalizacja atrybutów charakterystycznych
        dla samochodu elektrycznego.
        """
        super().__init__(make, model, year) # super od superklasy (nadrzędnej). Podrzędna -> podklasa.
        # Jest to funkcja pomagająca Pythonowi w utworzeniu połączenia między klasami.
        self.battery = Battery() # Ta linijka powoduje, że dla każdego egzemplarza klasy ElectricCar będzie tworzony egzemplarz klasy Battery.

    def fill_gas_tank(self): # Metoda o takiej samej nazwie jak w klasie Car. W ten sposób nadpisujemy metodę.
        """Samochody elektryczne nie mają zbiorników paliwa."""
        print("Ten samochód nie wymaga tankowania paliwa!")