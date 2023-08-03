# 4.7 Trzy. Utwórz listę liczb od 3 do 30 podniesionych do 3 potęgi, a następnie wyświetl zawartość listy za pomocą pętli for.
"""
lista = []

for liczba in range(3,31):
    lista.append(liczba**3)

print(lista)
"""

lista = [liczba**3 for liczba in range(3,31)]
print(lista)