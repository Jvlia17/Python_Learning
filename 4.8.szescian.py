# 4.8 Sześcian. Utwórz listę pierwszych dziesięciu sześcianów, a następnie wyświetl je za pomoca pętli for.

"""
lista = []
for liczba in range(1,11):
    lista.append(liczba**3)
print(lista)
"""

lista = [liczba**3 for liczba in range (1,11)]
print(lista)