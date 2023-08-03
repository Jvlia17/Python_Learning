# 3.7 Kurcząca się lista gości. Okazało się, że większy stół nie zostanie dostarczony na czasi dlatego masz mrijsce dla jedynie dwóch gości.

lista_gosci = ["Ania", "Szymon", "Milena"]
print(f"Zapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")

print(f"\nNiestety {lista_gosci[2]} nie da rady przyjść na obiad :(")

lista_gosci[2] = "Paulina"
print(f"\nZapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")

print("\nZnaleziono większy stół")

lista_gosci.insert(0, "Daniel")
lista_gosci.insert(2, "Kuba")
lista_gosci.append("Błażej")

print(f"\nZapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[3]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[4]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[5]}!")

print("\nJednak nie ma większego stołu, możesz zaprosić tylko dwie osoby :(")

print(f"\nPrzepraszam, jednak nie zapraszam Cie na obiad {lista_gosci.pop(0)}")
print(f"Przepraszam, jednak nie zapraszam Cie na obiad {lista_gosci.pop(1)}")
print(f"Przepraszam, jednak nie zapraszam Cie na obiad {lista_gosci.pop(2)}")
print(f"Przepraszam, jednak nie zapraszam Cie na obiad {lista_gosci.pop(2)}")

print(f"\nZapraszam Cię na obiad, {lista_gosci[0]}")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}")

del lista_gosci[0]
del lista_gosci[0]

print(lista_gosci)