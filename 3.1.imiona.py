"""
# Indeks listy [-1] zwraca zawsze ostatni jej element!
# A przykładowo [-3] zwraca trzeci element od końca
# Przydatne w sytuacjach, kiedy nie znamy ilości elementów na liście

rowery = ["trekingowy", "górski", "miejski", "szosowy"]
print(f"Ostatni rower na liście to: {rowery[-1].title()}")
"""

# 3.1 Imiona. Utwórz listę o nazwie names i umieść na niej imiona kilku przyjaciół. Wyświetl wszystkie imiona przez uzyskanie dostępu do poszczególnych elementów listy (za każdym razem do jednego).

names = ["szymon", "ania", "mola", "pola"]

print(names[0].title())
print(names[1].title())
print(names[-1].title())