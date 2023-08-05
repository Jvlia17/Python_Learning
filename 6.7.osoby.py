'''
alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'żółty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
# 3 słowniki umieszczone w liście

for alien in aliens:
    print(alien)

aliens = []

# Utworzenie 30 zielonych obcych
for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien) # dodawanie słownika do listy

# Wyświetlenie pierwszych pięciu obcych
for alien in aliens[:5]:
    print(alien)
print('...')

# Wyświetlenie całkowitej liczby utworzonych obcych
print(f"Całkowita liczba obcych: {len(aliens)}")

# pierwsi 3 obcy: na zolto , srednia, 10 pkt

for alien in aliens[:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['points'] = 10
        alien['speed'] = 'średnio'
    elif alien['color'] == 'żółty':
        alien['color'] = 'czerwony'
        alien['points'] = 15
        alien['speed'] = 'szybko'

for alien in aliens[:5]:
    print(alien)

pizza = {
    'crust' : 'grubym',
    'toppings': ['pieczarki', 'podwójny ser'], # lista w słowniku
}

#Podsumowanie zamówienia
print(f"Zamówiłeś pizzę na {pizza['crust']} cieście z "
    "następującymi dodatkami:") # Wow! Można tak dzielić printa :)

for topping in pizza['toppings']:
    print(f"\t{topping}")

# Lista w słowniku -> kiedy jeden argument ma więcej opcji
# Słownik w liście -> kiedy tworzymy dużo takich samych obiektów

favorite_language = {'janek': ['python', 'ruby'], # osoby maja przypisaną listę
                     'sara': ['c'],
                     'edward': ['ruby', 'go'],
                     'paweł': ['python', 'haskell'],
                     }

#for osoba in favorite_language.keys():
#    print(f"Ulubionym językiem programowania użytkownika {osoba.title()} to:")
#    print(f"{favorite_language[osoba]}")

for osoba, języki in favorite_language.items():
    if len(języki) == 1:
        print(f"Ulubiony język programowania użytkownika {osoba.title()} to {języki[0].title()}")
        # języki[0].title() aby ładnie wyświetlić język C
    else:
        print(f"Ulubionym językiem programowania użytkownika {osoba.title()} to:")
        for język in języki:
            print(f"\t{język.title()}")

users = { # słownik w słowniku
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maria',
        'last': 'skłodowska - curie',
        'location': 'paryż',
    },
}

for username, user_info in users.items():
    print(f"\nNazwa użytkownika: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tImie i nazwisko: {full_name.title()}")
    print(f"\tMiejscowość: {location}")
'''

# 6.7 Osoby. Pracę rozpocznij od programu stworzonego w ćwiczeniu 6.1 we wcześniejszej części rozdziału. Utwórz dwa nowe słowniki przedstawiające różne osoby, a następnie wszystkie trzy słowniki umieść na liście o nazwie people.

osoba_0 = {'first_name': 'Szymon', 'last_name': 'Krukowski', 'age': 22, 'city': 'Bogatynia'}
osoba_1 = {'first_name': 'Julia', 'last_name': 'Rzepka', 'age': 23, 'city': 'Leszno'}
osoba_2 = {'first_name': 'Ania', 'last_name': 'Sim', 'age': 23, 'city': 'Dobroszyce'}

people = [osoba_0, osoba_1, osoba_2]

for osoba in people:
    print(f"Imię: {osoba['first_name']}, nazwisko: {osoba['last_name']}, wiek: {osoba['age']}, miasto: {osoba['city']}")