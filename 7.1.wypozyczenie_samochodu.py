'''
message = input("Powiedz mi cos o sobie, a wyświetlę to na ekranie: ")
print(message)

name = input("Podaj swoje imię: ")
print(f"Witaj, {name}!")

# Jeśli chcemy wyświetlić dłuższy input message, to możemy to zrobić tak:
promt = "Jeżeli powiesz nam, kim jesteś, spersonalizujemy wyświetlany komunikat."
promt += "\nJak masz na imię? "

name = input(promt)
print(f"\nWitaj, {name}!")

# Ważne! Przy użyciu input() program traktuje dane wejściowe jako tekst!!! Więc liczby także potraktuje jako tekst.

age = input("Ile masz lat? ")
age = int(age) # konwertuje na wartości liczbowe
print(age >= 18)

height = input("Ile masz wzrostu (w centymentach)? ")
height = int(height)

if height >= 90:
    print("\nJesteś wystarczająco wysoki na przejażdżkę!")
else:
    print("\nBędziesz mógł sie przejechać, gdy nieco urośniesz.")

number = input("Podaj liczbę, aby dowiedzieć się czy jest parzysta czy nieparzysta: ")
number = int(number)

if number % 2 == 0:
    print(f"Liczba {number} jest parzysta.")
else:
    print(f"Liczba {number} nie jest parzysta.")
'''

# 7.1 Wypożyczenie samochodu. Utwórz program, który pyta użytkownika, jakiej marki samochód chciałby wypożyczyć.

marka = input("Jakiej marki samochód chciałbyś wypożyczyć? ")
print(f"Samochód marki {marka} jest dostępny do wypożyczenia.")