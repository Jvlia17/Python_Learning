# 15.4 Zmodyfikowane błądzenie losowe. W klasie RandomWalk wartości x_step i y_step są generowane na podstawie tego samego zestawu warunków. Kierunek jest wybierany losowo na podstawie listy [1, -1], natomiast odległość na podstawie listy [0, 1, 2, 3, 4].

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:
    # Przygotowanie danych do błądzenia losowego.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego.
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)

    # Dodanie, aby intensywność koloru oznaczaa jego kolejność -> efekt gradientu.
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    ax.scatter(0, 0, c='white', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolor='none', s=100)

    # Ukrycie osi w celu lepszej wizualizacji tego, co ważne.
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)

    plt.show()
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == 'n':
        break

# Wniosek: po zmianie kodu zgodnie z poleceniem widzimy wykres rosnący prawie liniowo. Wynika to stąd, że nie możemy się już ani w osi X ani Y cofać. Natomiast zwiększenie zakresu ruchu spowodowało wygenerowanie większych wartości.