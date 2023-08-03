# 4.12 Więcej pętli. We wszystkich programach foods.py przedstawionych w tym rozdziale uniknąłem użycia pętli for, aby zaoszczędzić nieco miejsca. Wybierz dowolną wersję programu foods.py, a następnie utwórz dwie pętle for w celu wyświetlenia obu list potraw.

my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
friend_foods = my_foods[:]

print("Moje ulubione potrawy to:")
for food in my_foods:
    print(food.title())

print("\nUlubione potrawy mojego przyjaciela to:")
for food in friend_foods:
    print(food.title())