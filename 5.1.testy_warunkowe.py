"""
samochody = ["audi", "bmw", "subaru", "toyota"]

for samochod in samochody:
    if samochod == "bmw":
        print(samochod.upper())
    else:
        print(samochod.title())

print("\n")

car = "audi"
print(car == "Audi") # False, ponieważ wielkośc liter w Pythonie ma znaczenie
print(car.title() == "Audi") # Tu mamy True, ponieważ tymczasowo zmieniliśmy pierwszą literę na wielką

requested_topping = "pieczarki"

if requested_topping != "anchois":
    print("\nPoproszę o anchois!\n")

wiek = 18
print(wiek == 18)
print(wiek <= 21)
print(wiek >= 15)

wiek_0 = 22
wiek_1 = 18

print((wiek_0 >= 21) and (wiek_1 >= 21)) # and - oba warunki musza być spełnione, aby wypluło true

wiek_1 = 21

print((wiek_0 >= 21) and (wiek_1 >= 21))

wiek_0 = 22
wiek_1 = 18

print((wiek_0 >= 21) or (wiek_1 >= 21)) # or - wystarczy, że jeden warunek jest prawdziwy

requested_toppings = ['pieczarki', 'cebula', 'ananas']
print('pieczarki' in requested_toppings) # poleceniem in możemy sprawdzić czy coś znajduje się na liście

zbanowani_uzytkownicy = ["andrzej", "blazej", "konrad"]
uzytkownik = "milena"

if uzytkownik not in zbanowani_uzytkownicy: # not in sprawdzamy czy coś znajduje się na liście
    print(f"Użytkownik {uzytkownik.title()} może publikować wiadomości na forum!")

game_active= True
can_edit = False
"""

# 5.1 Testy warunkowe. Utwórz serię testów warunkowych. Wyświetl polecenia opisujące poszczególne testy oraz przewidywany wynik.

kwiat = "magnolia"
print(f"1. Czy kwiat == 'magnolia'? Przewiduję wartość True")
print(kwiat == "magnolia")

wiek = 25
print(f"\n2. Czy wiek >= 30? Przewiduję wartość False")
print(wiek >= 30)

gracz_1 = "szymon"
gracze = ['milena', 'blazej', 'szymon', 'konrad']
print(f"\n3. Czy wśród graczy znajduje się Szymon? Przewiduje wartość True")
print(gracz_1 in gracze)

gracz_2 = "julia"
print(f"\n4. Czy wśród graczy znajduje się Julia? Przewiduję wartość False")
print(gracz_2 in gracze)

uczulenie = ['mleko', 'orzechy', 'chleb', 'sezam']
danie = 'melon'
print(f"\n5. Czy jest uczulenie na melona? Przewiduję False")
if danie not in uczulenie:
    print(False)
else:
    print(True)

danie = 'mleko'
print(f"\n6. Czy jest uczulenie na mleko? Przewiduję True")
if danie not in uczulenie:
    print(False)
else:
    print(True)


imiona_damskie = ['kasia', 'basia', 'maria']
imiona_meskie = ['karol', 'andrzej', 'maria']

print(f"\n7. Czy imię Maria jest i w imionach damskich i męskich? Przewiduję True")
if ('maria' in imiona_meskie) and ('maria' in imiona_damskie):
    print(True)
else:
    print(False)

print(f"\n8. Czy imię Karol jest i w imionach damskich i męskich? Przewiduję False")
if ('karol' in imiona_meskie) and ('karol' in imiona_damskie):
    print(True)
else:
    print(False)

print(f"\n9. Czy imię Karol jest w jakichkolwiek imionach? Przewiduję True")
if ('karol' in imiona_meskie) or ('karol' in imiona_damskie):
    print(True)
else:
    print(False)

print(f"\n10. Czy imię Karolina jest w jakichkolwiek imionach? Przewiduję False")
if ('karolina' in imiona_meskie) or ('karolina' in imiona_damskie):
    print(True)
else:
    print(False)

imie_1 = 'maciej'
imie_2 = 'Maciej'

print(f"\n11. Czy imię maciej i Maciej da taki sam wynik? Przewiduję False")
print(imie_1 == imie_2)

print(f"\n12. Czy imię maciej i Maciej z użyciej funkcji lower() da taki sam wynik? Przewiduję True")
print(imie_1 == imie_2.lower())