"""
even_numbers = list(range(2, 11, 2)) # pierwszy argument: wartość początkowa, drugi argument: wartość końcowa (-1), trzeci argument: co ile rośnie
print(even_numbers)

i = 0
potegi = []

for liczba in range(1,11):
    potegi.insert(liczba*liczba)

print(potegi)

liczby = range(0,100)
print(min(liczby))
print(max(liczby))
print(sum(liczby))

squares = [value**2 for value in range(1,11)] # lista składana - warto korzystać
print(squares)
"""

# 4.3 Odliczanie do dwudziestu. Użyj pętli for do wyświetlenia liczb od 1 do 20 włącznie.

for value in range(1, 21):
    print(value)