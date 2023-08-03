# 5.11 Liczby porządkowe. Liczby porządkowe wskazują położenie elementu na liście, na przykład pierwszy, drugi, trzeci. W języku angielskim większość kończy się na "th", poza liczbami 1, 2 i 3.

lista = list(range(1,10))

for liczba in lista:
    if liczba == 1:
        print('1st')
    elif liczba == 2:
        print('2nd')
    elif liczba == 3:
        print('3rd')
    else:
        print(f'{liczba}th')