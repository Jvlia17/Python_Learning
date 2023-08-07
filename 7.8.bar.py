'''
# nie powinno sie modyfikowac listy podczas iteracji for

unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

while unconfirmed_users: # jest wykonywana, dopóki lista zawiera jakiekolwiek elementy
    current_user = unconfirmed_users.pop()

    print(f"Weryfikacja użytkownika {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nZweryfikowano wymienionych poniżej użytkowników:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['pies', 'kot', 'królik', 'kot', 'pies', 'złota rybka', 'kot']
print(pets)

while 'kot' in pets:
    pets.remove('kot')

print(pets)


responses = {}

polling_active = True

while polling_active:
    name = input('\nJak masz na imię? ')
    response = input('Na który szczyt chciałbyś sie wspiąć pewnego dnia? ')

    responses[name] = response

    repeat = input('Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie) ')
    if repeat == 'nie':
        polling_active = False

print("\n --- Wyniki ankiety ---")
for name, response in responses.items():
    print(f"{name} chciałby się wspiąć na {response}")
'''

# 7.8 Bar. Przygotuj listę o nazwie sandwich_orders i umieść na niej nazwy różnych kanapek. Następnie przygotuj pustą listę o nazwie finished_sandwiches.

sandwich_orders = ['z szynką', 'z serem', 'z tuńczykiem', 'z boczkiem', 'z jajkiem']
finished_sandwiches = []

while sandwich_orders: # dopóki lista nie jest pusta
    current_sandwich = sandwich_orders.pop()
    print(f"Aktualnie przygotowuję kanapkę {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nOto wszystkie zrobione dzisiaj kanapki: ")
for sandwich in finished_sandwiches:
    print(f"\tKanapka {sandwich}")