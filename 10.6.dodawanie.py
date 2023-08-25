'''
# print(5/0) # Python wyrzuci stos wywołań informujący o obiekcie wyjątku, który stworzył w odpowiedzi na niemożliwość wykonania kodu.

# Dzięki używaniu try-except możemy kontynuować działanie programu po wystąpieniu błędu oraz zapewniamy użytkownikowi komfort w odczytaniu błędu, a nawet możliwość poprawy wprowadzonych danych!
try:
    print(5/0)
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")

print("Podaj dwie liczby, które zostaną podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu.")
while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("\nDruga liczba: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number) # Ważne jest, aby w bloku try znajdował się tylko kod, który może potencjalnie powodować błędy (inaczej zgłoszenie wyjątku).
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")
    else:
        print(answer)

def count_words(file):
    """Obliczanie przybliżonej liczby słów w danym pliku."""

    try:
        with open(file, encoding='utf-8') as f:  # encoding -> gdy domyślne kodowanie znaków w systemie nie odpowiada kodowaniu znaków w otwieranym pliku
            contents = f.read()
    except FileNotFoundError:
        pass # tak zwane ciche niepowodzenie -> nie informujemy o błędzie i kontynuujemy pracę programu jak gdyby nigdy nic
    else:  # każdy fragment kodu, którego wykonanie zależy od zakończonego powodzeniem bloku try, powinien znaleźć się w else.
        words = contents.split()
        num_words = len(words)
        print(f"Plik {filename} zawiera {num_words} słów.")

filenames = ['pliki_tekstowe/alice.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)
'''

# 10.6 Dodawanie. Jeden z najczęściej pojawiających się problemów podczas pobierania danych liczbowych polega na tym, że użytkownicy podają tekst zamiast liczb.

print("Program do dodawania dwóch liczb\n")

first_number = input("Pierwsza liczba: ")
second_number = input("Druga liczba: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    answer = first_number + second_number  # answer musi być tu, bo będąc w bloku else podaje jedną z liczb jako odpowiedź, jeśli druga nie jest liczbą
except ValueError:
    print("Któraś z podanych wartości nie jest liczbą!")
else:
    print(answer)
