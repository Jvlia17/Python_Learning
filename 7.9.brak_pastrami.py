# 7.9 Brak pastrami. Wykorzystaj listę sandwich_orders z ćwiczenia 7.8 i upewnij się, że na liście przynajmniej trzykrotnie pojawia się kanapka z pastrami.

sandwich_orders = ['z szynką', 'z pastrami','z serem', 'z tuńczykiem', 'z pastrami', 'z boczkiem', 'z jajkiem', 'z pastrami']
finished_sandwiches = []

print("Przepraszamy, niestety kanapka z pastrami jest niedostępna.\n")

while 'z pastrami' in sandwich_orders:
    sandwich_orders.remove('z pastrami')

while sandwich_orders: # dopóki lista nie jest pusta
    current_sandwich = sandwich_orders.pop()
    print(f"Aktualnie przygotowuję kanapkę {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nOto wszystkie zrobione dzisiaj kanapki: ")
for sandwich in finished_sandwiches:
    print(f"\tKanapka {sandwich}")