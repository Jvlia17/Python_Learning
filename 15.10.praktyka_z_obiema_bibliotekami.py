# 15.10 Praktyka z obiema bibliotekami. Spróbuj użyć biblioteki matplotlib do utworzenia wizualizacji rzutów kośćmi do gry oraz plotly do przygotowania wizualizacji błądzenia losowego.

from die import Die
from matplotlib import pyplot as plt

die = Die(6)

results = [die.roll() + die.roll() for roll_num in range(1000)]

plt.title('Częstotliwośc występowania wartości')
plt.xlabel('Wynik')
plt.ylabel('Częstotliwość')
plt.hist(results, bins=range(2, 14), rwidth=0.8)
plt.show()

from random_walk import RandomWalk
import plotly.express as px

rw = RandomWalk(1000)
rw.fill_walk()

fig = px.scatter(rw.x_values, rw.y_values)
fig.show()