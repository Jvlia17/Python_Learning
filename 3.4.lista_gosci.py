"""
# Lista dynamiczna - lista, której elementy będa się zmieniać, będa usuwane lub dodawane

kwiaty = ["hiacynt", "róża", "tulipan"]
print(kwiaty)

kwiaty[0] = "storczyk" # zmiana elementu listy
print(kwiaty)

kwiaty.append("storczyk") # dodanie elementu do końca listy
print(kwiaty)

kwiaty = [] # pusta lista
kwiaty.append("hiacynt")
kwiaty.append("róża")
kwiaty.append("tulipan")
print(kwiaty)

kwiaty = ["hiacynt", "róża", "tulipan"]
kwiaty.insert(2, "storczyk") # wstawianie elementów na wskazane pozycje, reszta sie przesuwa
print(kwiaty)

kwiaty = ["hiacynt", "róża", "tulipan"]
del kwiaty[0] # usuwanie elementu z listy o podanym indeksie
print(kwiaty)

kwiaty = ["hiacynt", "róża", "tulipan"]
# popped_kwiat = kwiaty.pop() # usuwanie elementu z listy o wskazanym indeksie z możliwością jego przechowywania
# print(popped_kwiat)

print(f"Moje ulubione kwiaty to {kwiaty.pop(1)}")
print(kwiaty)

kwiaty = ["hiacynt", "róża", "tulipan"]
uczulenie = "tulipan"
kwiaty.remove(uczulenie) # metodą remove usuwamy pierwszy znaleziony element listy o wskazanej nazwie
print(kwiaty)
print(f"Kwiat {uczulenie} został usunięty, ponieważ uczula")
"""

# 3.4 Lista gości. Jeżeli mógłbyś zaprosić kogokolwiek na obiad, żyjącego lub nieżyjącego, to kogo byś zaprosił? Utwórz listę zawierająca przynajmniej trzy osoby, które chciałbyś zaprosić na obiad. Następnie wykorzystaj tę listę do wyświetlenia dla każdej z tych osób komunikatu zapraszającego na obiad.

lista_gosci = ["Ania", "Szymon", "Milena"]
print(f"Zapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")
