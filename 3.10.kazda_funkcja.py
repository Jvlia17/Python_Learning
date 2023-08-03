# 3.10 Każda funkcja. Zastanów się, jakie informacje mógłbyś umieścić na liście. Na przykład utwórz listę gór, rzek, państw, miast, języków lub czegokolwiek innego. Przygotuj program, który będzie tworzył listę przechowywującą te informacje i używał co najmniej jeden raz każdej funkcji wprowadzonej w tym rozdziale.

lista_miast = ["Wrocław", "Leszno", "Kołobrzeg", "Zielona góra", "Karpacz", "Czarnogóra"]

# print
print(lista_miast[-1])

# zmiana wartości
lista_miast[4] = "Świdnica"

# append
lista_miast.append("Góra")

# insert
lista_miast.insert(0, "Białystok")

# del
del lista_miast[1]

# pop
lista_miast.pop()

# remove
lista_miast.remove("Leszno")

# sort
lista_miast.sort(reverse=True)

# sorted
sorted(lista_miast)

print(lista_miast)

