# Słownik jest kolekcją par klucz - wartość
# Słownik jest dynamiczny - w trakcie działania kodu można zmieniac jego zawartość
# [] - lista
# () - krotka
# {} - słownik

'''
alien_0 = {'color': 'zielony', 'points': 5} # słownik = {klucz : wartość, klucz : wartość}

# print(alien_0['color'])
# print(alien_0['points'])

# points = alien_0['points']
print(f"Gratulacje! Zdobyłeś {alien_0['points']} punktów!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {} # tworzymy pusty słownik
alien_1['color'] = 'zielony'
alien_1['points'] = 5

print(f'Obcy ma kolor {alien_1["color"]}')

alien_1['kolor'] = 'żółty'

print(f"Obcy ma teraz kolor {alien_1['kolor']}")

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'średnio', 'points' : 5}
print(f'Początkowa wartość x-position: {alien_2["x_position"]}')

# Przesunięcie obcego w prawo
# Ustalenie odległości, jaką powinien pokonać obcy poruszający się z daną szybkością.

if alien_2['speed'] == 'wolno':
    x_increment = 1
elif alien_2['speed'] == 'średnio':
    x_increment = 2
else:
    x_increment = 3

# Nowe położenie to suma dotychczasowego położenia i wartości x_increment.
alien_2['x_position'] += x_increment

print(f"Nowa wartość x-position: {alien_2['x_position']}")

print(alien_2)

del alien_2['points'] # usuwanie klucza ze słownika

print(alien_2)

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

print(f'Ulubiony język programowania Sary to {favorite_languages["sara"].title()}')

alien_3 = {'color': 'zielony', 'speed': 'wolny'}

point_value = alien_3.get('points', 'Brak przypisanych punktów') # Do zdefiniowania wartości domyślnej, która będzie zwrócona, jeśli klucz nie instnieje.

print(point_value)
'''

# 6.1 Osoba. Wykorzystaj słownik do przechowywania informacji o znanej Ci osobie. W słowniku powinny się znaleźc informacje takie, jak imię, nazwisko, wiek i miasto zamieszkania.

osoba = {'first_name': 'Szymon', 'last_name': 'Krukowski', 'age': 22, 'city': 'Wrocław'}

print(osoba)