'''
def greet_user(username): # definicja funkcji (parametr)
    """Wyświetla proste powitanie."""
    # To wyżej to docstring, jego zadaniem jest opisanie działania funkcji -> jest potem dodawany automatycznie przez Pythona przy generowaniu dokumentacji
    print(f"Witaj, {username.title()}!")

greet_user('janek') # wywołanie funkcji (argument)
greet_user('sara')

# parametr - fragment informacji, który jest wymagany przez funkcję, aby mogła wykonac przypisane jej zadanie
# argument - fragment informacji przekazywany z wywołaniem funkcji do treści funkcji
# parametr i argument często sa używane wymiennie
'''

# 8.1 Komunikat. Utwórz funkcję o nazwie display_messages() wyświetlającą jedno zdanie informujące o tym, czego się uczysz w tym rozdziale.

def display_messages():
    """Wyświetla wiadomość o tym, czego się ucze w tym rozdziale."""
    print("W tym rozdziale uczę się poprawnego definiowania i używania funkcji.")

display_messages()