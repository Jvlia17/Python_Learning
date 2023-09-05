# 15.1 Sześciany. Liczba podniesiona do trzeciej potęgi jest sześcianem. Wygeneruj wykres dla sześcianów pierwszych pięciu liczb, a następnie przygotuj wykres dla sześcianów poierwszych 500 liczb.

import matplotlib.pyplot as plt

plt.style.use('ggplot')

x_values = list(range(1, 501))
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='pink', s=10)

ax.set_title("Sześciany liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Sześciany wartości", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
