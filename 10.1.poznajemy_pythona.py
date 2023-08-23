'''
filename = 'pliki_tekstowe\pi_digits.txt'
with open(filename) as file_object: # Wywołanie funkcji open() zwraca obiekt reprezentujący plik, a następnie zapisujemy go pod nazwą file_object.
    contents = file_object.read() # Za pomocą .read() wczytujemy całą zawartość pliku tekstowego file_object i zapisujemy ją w długim ciągu tekstowym 'contents'.
print(contents)

# 'with' na początku kodu powoduje zamknięcie pliku, gdy dostęp do niego nie będzie już potrzebny.
# Jest to super podejście -> istnieje funkcja close(), ale w przypadku błędu w kodzie, możemy nawet stracić nasze dane.
# W skrócie -> 'with open' to super wyjście.

# Funkcja read() powoduje dodanie na końcu ciągu tekstowego dodatkowego wiersza.
print(contents.rstrip())

# Ciekawostka -> możemy równie dobrze napisać 'pliki_tekstowe\pi_digits.txt' jak i 'pliki_tekstowe/pi_digits.txt'.

file_path = "C:\\Users\\szylk\\Desktop\\pi_digits.txt"
# Ważne! Można po prostu użyć opcji -> 'Kopiuj jako ścieżkę', ale wtedy zamiast pojedynczego znaku \ trzeba dac dwa \\.

with open(file_path) as file_object:
    for line in file_object: # przeprowadzamy iterację wiersz po wierszu
        print(line.rstrip())

filename = 'pliki_tekstowe\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # Każdy element listy lines odpowiada jednemu wierszowi w pliku.

for line in lines:
    print(line.rstrip())

filename = 'pliki_tekstowe\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # Każdy element listy lines odpowiada jednemu wierszowi w pliku.

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = 'pliki_tekstowe/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"Pierwsze 50 liczb w liczbie pi: {pi_string[:51]}")

filename = 'pliki_tekstowe/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Podaj swoją datę urodzenia w formacie ddmm: ")
if birthday in pi_string:
    print("Twoje urodziny znajdują się w pierwszych stu tysiącach cyfr liczby pi!")
else:
    print("Twoich urodzin nie ma w pierwszych stu tysiącach cyfr liczby pi.")
'''

# 10.1 Poznajemy Pythona. W edytorze tekstu utwórz pusty plik i wpisz w nim kilka zdań podsumowujących to, czego się dotąd nauczyłes o języku Python.

filename = 'pliki_tekstowe/learning_python.txt'

with open(filename) as file_object1: # Poprzez odczytanie całego pliku.
    contents = file_object1.read()
print(contents)

print("\n")

with open(filename) as file_object2: # Poprzez iterację przez obiekt pliku.
    for line in file_object2:
        print(line.strip())

print("\n")

with open(filename) as file_object3: # Poprzez umieszczenie wierszy na liście.
    lines = file_object3.readlines()
for line in lines:
    print(line.strip())