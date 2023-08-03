"""
wiek = 17
if wiek >= 18:
    print('Możesz wziąc udział w głosowaniu!')
    print('Czy zarejestrowałes się już, aby móc głosować?')
else:
    print('Przykro nam, ale jesteś zbyt młody, aby móc głosować.')
    print('Możesz się zarejestrowac po ukończeniu 18 lat!')

wiek = 66
# algorytm wejdzie do pierwszej znalezionej odpowiedzi bez sprawdzania reszty

if wiek < 4:
    cena = 0
elif wiek < 18:
    cena = 25
elif wiek < 65:
    cena = 40
elif wiek > 65: # warto unikać else z powodu nieprawidłowych lub złośliwych danych
    cena = 20

print(f'Bilet wstępu kosztuje {cena} złotych')

requested_toppings  = ['pieczarki', 'pepperoni', 'podwójny ser']

if 'pieczarki' in requested_toppings:
    print('Dodaję pieczarkę')             # tu elif i else nie zadziała
if 'pepperoni' in requested_toppings:
    print('Dodaję pepperoni')
if 'podwójny ser' in requested_toppings:
    print('Dodaję podwójny ser')
"""

# 5.3 Kolory obcych, część 1. Wyobraź sobie zestrzelenie obcego w grze. Utwórz zmienną o nazwie alien_color i orzypisz jej wartość 'zielony', 'żółty' lub 'czerwony'

alien_color = 'czerwony'

if alien_color == 'zielony':
    print('Gratulacje! Zdobywasz 5 punktów.')
elif alien_color == 'żółty':
    print('Gratulacje! Zdobywasz 10 punktów.')
elif alien_color == 'czerwony':
    print('Gratulacje! Zdobywasz 15 punktów.')