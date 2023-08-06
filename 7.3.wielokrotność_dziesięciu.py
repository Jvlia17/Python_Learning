# 7.3 Wielokrotność dziesięciu. Popros użytkownika o podanie dowolnej liczby, a następnie sprawdź, czy jest ona wielokrotnością liczby 10.

number = input("Podaj dowolna liczbę: ")
number = int(number)

if number % 10 == 0:
    print(f"Liczba {number} jest wielokrotnością 10.")
else:
    print(f"Liczba {number} nie jest wielokrotnością 10.")