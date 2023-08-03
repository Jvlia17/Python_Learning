'''
requested_toppings = ['boczek', 'podwójny ser', 'pieczarki']

for topping in requested_toppings:
    if topping == 'boczek':
        print('Niestety nie mamy boczku')
    else:
        print(f'Dodaję {topping}')
print('\nTwoja pizza jest już gotowa!')

requested_toppings = []

if requested_toppings: # zwraca True, jeśli lista zawiera chociaz jeden element. W przypadku pustej listy zwróci False.
    for topping in requested_toppings:
        print(f'Dodaję {topping}')
    print('Twoja pizza jest gotowa!')
else:
    print('Czy jesteś pewien, że chcesz pizzę bez dodatków?')

available_toppings = ('szynka', 'pieczarki', 'pepperoni', 'podwójny ser', 'oliwki', 'boczek')
# tutaj dane moga byc w krotce, bo się nie zmienią dostępne składniki

requested_toppings = ['szynka', 'pieczarki', 'frytki']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f'Dodaję {topping} do pizzy!')
    else:
        print(f'Niestety obecnie nie mamy dodatku {topping}.')
print('\nTwoja pizza jest gotowa!')
'''

# 5.8 Witaj, administratorze. Przygotuj listę przynajmniej pięciu nazw użytkowników, zawierającą między innymi nazwę 'admin'. Wyobraź sobie, że tworzysz kod odpowiedzialny za powitanie użytkownika po jego zalogowaniu się w witrynie internetowej. Przeprowadź iterację przez pętlę i dla każdego użytkownika wyświetl powitanie.

nazwy_uzytkownikow = ['kasia', 'malymarcel', 'skromnaoliwka', 'admin', 'bluszcz89']

for uzytkownik in nazwy_uzytkownikow:
    if uzytkownik == 'admin':
        print(f'Witaj, {uzytkownik}! Czy chcesz przejrzeć dzisiejszy raport?')
    else:
        print(f'Witaj, {uzytkownik}! Dziękujemy, że ponownie się zalogowałeś')