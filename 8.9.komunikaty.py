# przekazywanie listy do funkcji to inaczej przekazanie funkcji dostępu do tej listy (nawet z możliwością edycji)

'''
def greet_users(names):
    """Wyświetla proste powitanie każdemu użytkownikowi z listy."""
    for name in names:
        msg = f"Witaj, {name.title()}!"
        print(msg)

usernames = ['halina', 'tymek', 'marzena']
greet_users(usernames) # przekazanie listy do funkcji

def print_models(unprinted_designs, completed_models):
    """Symuluje wydruk projektów."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Wyświetla wszystkie modele, które zostały wydrukowane."""
    print("\nWydrukowane zostały następujące modele: ")
    for model in completed_models:
        print(model)

unprinted_designs = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_models = []

# Możemy postanowić, że z jakiegos konkretnego powodu nie chcemy pracowac na liście unprinted_designs.
# W takim wypadku możemy zapisac jak poniżej unprinted_models[:] i wtedy pracujemy na kopii tej listy
# Jednakże musi byc ku temu konkretny powód, inaczej niepotrzebnie zużywamy czas i pamięć programu.

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Każda funkcja ma jasne zadanie. Kiepską praktyką jest robienie funkcji, która wykonuje dużo zadań -> wprowadza to niepotrzebny chaos.
'''

# 8.9 Komunikaty. Przygotuj listę zawierającą serię krótkich komunikatów, a następnie przekaż ją do funkcji o nazwie show_messages(), która powinna wyświetlić każdy komunikat umieszczony na liście.

def show_messages(messages):
    """Wyświetla krótkie komunikaty."""
    for message in messages:
        print(message)

messages = ['pij dużo wody', 'chroń skórę przed słońcem', 'uważaj na dzikie zwierzęta']
show_messages(messages)