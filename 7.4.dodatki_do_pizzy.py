'''
# while działa dopóty, dopóki zdefiniowany warunek przyjmuje wartość True.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

promt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie: "
promt += "\nNapisz 'koniec', aby zakończyć działanie programu. "
message = "" # musimy mieć wartość początkową, aby wejść do pętli while
while message != 'koniec':
    message = input(promt)

    if message != 'koniec': # aby nie wyświetlać 'koniec' na końcu
        print(message)

promt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie: "
promt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

active = True
while active: # dopóki active == True, pętla będzie się wykonywać
    message = input(promt)

    if message == 'koniec':
        active = False
    else:
        print(message)

promt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie: "
promt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

while True: # dopóki active == True, pętla będzie się wykonywać
    message = input(promt)

    if message == 'koniec':
        break
    else:
        print(message)
# break można też zastosowac w iteracji for

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # nakazuje zignorowanie dalszej części polecenia (wraca na początek)
    print(current_number)

# w przypadku użyciu continue, w przeciwieństwie do break, wracamy na początek pętli, zamiast całkowicie ją zrywać
'''

# 7.3 Dodatki do pizzy. Utwórz pętlę proszącą użytkownika o podanie serii dodatków do pizzy.

# 1. Z użyciem break
promt = "Jeśli chcesz wyjść, wpisz 'koniec'"
promt += "\nJaki dodatek do pizzy sobie życzysz? "

while True:
    dodatek = input(promt)
    if dodatek != 'koniec':
        print(f"\tDodano {dodatek}!")

    else:
        break

'''
# 2. Z użyciem active = True
promt = "Jeśli chcesz wyjść, wpisz 'koniec'"
promt += "\nJaki dodatek do pizzy sobie życzysz? "
active = True

while active:
    dodatek = input(promt)
    if dodatek != 'koniec':
        print(f"\tDodano {dodatek}!")

    else:
        active = False
'''

'''
# 3. Z użyciem continue
promt = "Jeśli chcesz wyjść, wpisz 'koniec'"
promt += "\nJaki dodatek do pizzy sobie życzysz? "

while True:
    dodatek = input(promt)
    if dodatek != 'koniec':
        print(f"\tDodano {dodatek}!")
        continue
    break
'''