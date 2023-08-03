# 3.6 Więcej gości. Znalazłeś większy stół, co oznacza więcej miejsca dla gości. Zastanów się więc nad jeszcze trzema osobami, które mógłbyś zaprosić na obiad.

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