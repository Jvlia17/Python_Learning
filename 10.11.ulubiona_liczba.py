'''
# Format JSON (JavaScript Object Notation) został pierwotnie opracowany dla języka JavaScript, ale szybko stał sie powszechnie używanym formatem.
# W formacie JSON zapisujemy dane od użytkownika (np. preferencje w grze) w formie list i słowników.

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'pliki_tekstowe/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f) # dwa argumenty -> dane przeznaczone do zapisania oraz obiekt pliku, gdzie mają być umieszczone

with open(filename) as f: # domyślnie 'r'
    loaded_numbers = json.load(f) # jeden argument -> obiekt, z którego pobieramy dane

print(loaded_numbers)

# refaktoryzacja -> podział kodu na serię funkcji, aby kod stał się bardziej przejrzysty i prostszy do zrozumienia oraz łatwiejszy do rozbudowy
import json

def get_stored_username():
    """Pobranie imienia z pliku, o ile taki istnieje."""
    filename = 'username.json'
    try:
        with open(f"pliki_tekstowe/{filename}") as f:  # domyślnie 'r'
            username = json.load(f)
    except FileNotFoundError:
        return None # Dobra praktyka -> funkcja zwraca oczekiwaną wartość albo None.
    else:
        return username

def get_new_username():
    """Poproszenie użytkownika, aby podał swoje imię, a następnie zapisanie tego imienia w pliku."""
    username = input("Jak masz na imię? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    username = get_stored_username()
    if username:
        print(f"Witamy ponownie, {username}!")
    else:
        username = get_new_username()
        print(f"Twoje imię zostało zapisane i będzie używane później, {username}!")

greet_user()
'''

# 10.11 Ulubiona liczba. Utwórz program, który prosi użytkownika o podanie ulubionej liczby.

import json

file_path = "pliki_tekstowe/fav_numb.json"


def write_number():
    """Zapisuje ulubiona liczbę w pliku."""
    number = input("Jaka jest twoja ulubiona liczba? ")
    number = int(number)

    with open(file_path, 'w') as f:
        json.dump(number, f)


def read_number():
    """Odczytuje ulubioną liczbę."""
    with open(file_path) as f:
        fav_numb = json.load(f)
    print(f"Twoja ulubiona liczba to: {fav_numb}")


write_number()
read_number()
