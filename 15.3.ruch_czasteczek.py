# 15.3 Ruch cząsteczek. Zmodyfikuj rw_visual.py i zastąp wywołanie ax.scatter() wywołaniem ax.plot().

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:
    # Przygotowanie danych do błądzenia losowego.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego.
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)

    # Dodanie, aby intensywność koloru oznaczaa jego kolejność -> efekt gradientu.
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3, color='pink')

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    ax.scatter(0, 0, c='white', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Ukrycie osi w celu lepszej wizualizacji tego, co ważne.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == 'n':
        break