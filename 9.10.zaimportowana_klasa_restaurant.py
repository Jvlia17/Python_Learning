'''
# import car
# from electric_car import ElectricCar as EC
from car import Car, ElectricCar
# W tym momencie klasę Car i ElectricCar możemy używać, jakby została zdefiniowana w bieżącym pliku programu.
# from car import * -> to podejście nie jest polecane, ponieważ nie widzimy jakie moduły pobieramy i możliwe, że pobierzemy klasę o nazwie, która już istnieje w naszym pliku, co będzie trudne do znalezienia i naprawienia.

my_beetle = Car('volkswagen', 'beetle', 2019)
# my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla = ElectricCar('tesla', 'roadster', 2019)
# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
'''

# 9.10 Zaimportowana klasa Restaurant. Przenieś do modułu ostatnią wersję klasy Restaurant i uwtórz oddzielny plik importujący tę klasę.
from restaurant import Restaurant

restaurant = Restaurant('Bon Yun Bi', 'koreańska')

print(f"Restauracja polecana na dzisiaj to {restaurant.restaurant_name}!")
print(f"Jest to restauracja {restaurant.cuisine_type}.\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
