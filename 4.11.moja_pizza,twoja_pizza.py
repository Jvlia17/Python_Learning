# 4.11 Moja pizza, Twoja pizza. Pracę rozpocznij od programu utworzonego w ćwiczeniu 4.1 we wcześniejszej cześci rozdziału. Utwórz kopię listy z pizzami i nadaj jej nazwę friend_pizzas, Teraz wykonas wymienione zadania.

pizzas = ["margherita", "crudo e rucola", "capricciosa"]
friend_pizzas = pizzas[:]

pizzas.append("cztery sery")
friend_pizzas.append("gorgonzola")

print("Moje ulubione rodzaje pizzy to:")
for pizza in pizzas:
    print(pizza.title())

print("\nUlubione rodzaje pizzy mojego przyjaciela to:")
for pizza in friend_pizzas:
    print(pizza.title())