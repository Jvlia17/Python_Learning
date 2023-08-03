"""
przyjaciele = ["Ania", "Szymon", "Milena", "Paulina"]

print("Oto dwójka moich najbliższych przyjaciół:")

for przyjaciel in przyjaciele[0:2]:
    print(przyjaciel)

moje_ulubione_jedzenie = ["pizza", "sushi", "tortilla", "ramen"]
ulubione_jedzenie_przyjaciela = moje_ulubione_jedzenie[:] # pobieram całą listę. Musi być [:], inaczej tylko zmieniamy nazwę tej samej listy

print(moje_ulubione_jedzenie)
print(ulubione_jedzenie_przyjaciela)

moje_ulubione_jedzenie.append("tosty")
ulubione_jedzenie_przyjaciela.append("kebab")

print(moje_ulubione_jedzenie)
print(ulubione_jedzenie_przyjaciela)
"""

# 4.10 Wycinki. Pracę rozpocznij od jednego z programów utworzonych w tym rozdziale, a następnie na końcu dodaj kilka wierszy kodu wykonującego wymienione zadania.

moje_ulubione_jedzenie = ["pizza", "sushi", "tortilla", "ramen", "lody", "ryba", "sajgonki", "pad thai"]

print("Pierwsze trzy elementu listy to:")
for jedzenie in moje_ulubione_jedzenie[:3]:
    print(jedzenie.title())

print("\nTrzy elementy w środku listy to:")
for jedzenie in moje_ulubione_jedzenie[2:5]:
    print(jedzenie.title())

print("\nOstatnie trzy elementy listy to:")
for jedzenie in moje_ulubione_jedzenie[-3:]: # nie [-3:-1]
    print(jedzenie.title())