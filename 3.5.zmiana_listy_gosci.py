# 3.5. Zmiana listy gości. Dowiedziałeś się, że jedna z zaproszonych osób nie może przyjść na obiad. Konieczne jest więc wysłanie następnych zaproszeń. Zastanów się, kogo w takim razie jeszcze zaprosisz.

lista_gosci = ["Ania", "Szymon", "Milena"]
print(f"Zapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")

print(f"\nNiestety {lista_gosci[2]} nie da rady przyjść na obiad :(")

lista_gosci[2] = "Paulina"
print(f"\nZapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")