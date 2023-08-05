# 6.10 Ulubione liczby. Zmodyfikuj program utworzony w ćwiczeniu 6.2 we wcześniejszej części rozdziału. Po zmianach każda osoba może mieć więcej niż tylko jedną ulubioną liczbę,

ulubione_liczby = {'Milena': [69, 96],
                   'Szymon': [13, 68, 0],
                   'Julia': [17, 13, 44, 100],
                   'Paulina': [27, 23, 41],
                   'Ania': [21],
                   }

for osoba, liczby in ulubione_liczby.items():
    if len(liczby) == 1:
        print(f"Ulubioną liczbą osoby {osoba} jest {liczby[0]}")
    else:
        print(f"Ulubionymi liczbami osoby {osoba} są:")
        for liczba in liczby:
            print(f"\t{liczba}")