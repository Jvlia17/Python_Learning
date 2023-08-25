# 10.13 Weryfikacja użytkownika. W ostatniej wersji programu remember_me.py przyjęto założenie, że użytkownik już wcześniej podał swoje imię, lub też program został uruchomiony po raz pierwszy.

import json

def get_stored_username():
    """Pobranie imienia z pliku, o ile taki istnieje."""
    filename = 'pliki_tekstowe/username.json'
    try:
        with open(filename) as f:  # domyślnie 'r'
            username = json.load(f)
    except FileNotFoundError:
        return None # Dobra praktyka -> funkcja zwraca oczekiwaną wartość albo None.
    else:
        return username

def get_new_username():
    """Poproszenie użytkownika, aby podał swoje imię, a następnie zapisanie tego imienia w pliku."""
    username = input("Jak masz na imię? ")
    filename = 'pliki_tekstowe/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"Twoje imię zostało zapisane i będzie używane później, {username}!")
    return username

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    username = get_stored_username()
    if username:
        answer = input(f"Czy twoje imię to: {username}? (tak/nie) ")
        if answer == 'tak':
            print(f"Witamy ponownie, {username}!")
        elif answer == 'nie':
            username = get_new_username()
        else:
            print("Nie zaznaczyłeś żadnej odpowiedzi!")
    else:
        username = get_new_username()

greet_user()