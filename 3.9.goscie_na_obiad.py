# 3.9 Goście na obiad. Pracę rozpocznij od jednego z programów utworzonych w ćwiczeniach od 3.4 do 3.7. Za pomocą funkcji len() wyświetl komunikat wskazujący liczbe osób, które zostały zaproszone na obiad.

lista_gosci = ["Ania", "Szymon", "Milena"]
print(f"Zapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")

print(f"\nNiestety {lista_gosci[2]} nie da rady przyjść na obiad :(")

lista_gosci[2] = "Paulina"
print(f"\nZapraszam Cię na obiad, {lista_gosci[0]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[1]}!")
print(f"Zapraszam Cię na obiad, {lista_gosci[2]}!")

print(f"\nLiczba osób zaproszonych na obiad: {len(lista_gosci)}")