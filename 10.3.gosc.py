"""
file_path = 'pliki_tekstowe/programming.txt'

with open(file_path, 'w') as file_object: # Przez 'w' informujemy Pythona, że plik ma zostać otworzony w trybie zapisu.
    file_object.write("Uwielbiam programować!\n")
    file_object.write("Uwielbiam tworzyc nowe gry.\n")

# 'r' - odczyt
# 'w' - zapis
# 'a' - dołączanie
# 'r' - odczyt i zapis
# Jeśli nie podany żadnego argumentu -> domyślnie jest tryb odczytu.

# Jeśli plik nie istnieje, a mamy wybrany tryb zaposu -> Python sam stworzy plik.
# Uwaga! Otwieranie pliku w trybie zapisu kasuje poprzednią zawartość pliku!

with open(file_path, 'a') as file_object: # Teraz za pomocą 'a' otwieramy plik w trybie dołączania -> zawartość się nie kasuje.
    file_object.write("Uwielbiam odnajdywać elementy w ogromnych zbiorach danych.\n")
    file_object.write("Uwielbiam tworzyć aplikacje uruchamiane w przeglądarce internetowej.")
"""

# 10.3. Gość. Utwórz program, który prosi użytkownika o podanie imienia. Gdy użytkownik je wprowadzi, zapisz to imię w pliku o nazwie guest.txt.

name = input("Jak masz na imię? ")
file_path = 'pliki_tekstowe/guest.txt'

with open(file_path, 'w') as file_object:
    file_object.write(name.title())