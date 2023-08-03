# 5.9 Brak użytkowników. Do przygotowanegow poprzednim ćwiczeniu pliku dodaj polecenie if sprawdzające, czy lista użytkowników nie jest pusta.

nazwy_uzytkownikow = []

if nazwy_uzytkownikow:
    for uzytkownik in nazwy_uzytkownikow:
        if uzytkownik == 'admin':
            print(f'Witaj, {uzytkownik}! Czy chcesz przejrzeć dzisiejszy raport?')
        else:
            print(f'Witaj, {uzytkownik}! Dziękujemy, że ponownie się zalogowałeś')
else:
    print('Musimy znaleźć jakichś użytkowników!')