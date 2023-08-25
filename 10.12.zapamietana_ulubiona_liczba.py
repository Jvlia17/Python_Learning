# 10.12 Zapamiętana ulubiona liczba. Oba programy utworzone w poprzednim ćwiczeniu połącz w jednym pliku.

import json

file_path = "pliki_tekstowe/fav_numb.json"


def write_number():
    """Zapisuje ulubioną liczbę w pliku."""
    number = input("Jaka jest twoja ulubiona liczba? ")
    number = int(number)
    with open(file_path, 'w') as f:
        json.dump(number, f)

    print("Zapamiętam to!")


def read_number():
    """Odczytuje wartość ulubionej liczby lub None w przypadku braku pliku."""
    try:
        with open(file_path) as f:
            fav_numb = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_numb


def main():
    """Główny trzon programu."""
    fav_numb = read_number()
    if fav_numb:
        print(f"Twoja ulubiona liczba to: {fav_numb}")
    else:
        write_number()


main()
