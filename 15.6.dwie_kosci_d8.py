# 15.6 Dwie kości D8. Przygotuj symulację pokazującą, co się stanie, jeśli 1000 razy rzucisz dwiema kośćmi do gry mającymi po osiem ścianek.

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die(8)

results = []
for roll_num in range(1000):
    result = die.roll() + die.roll()
    results.append(result)

frequencies = []
max_result = die.num_sides + die.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1} # dtick : 1 -> nakazanie dodawania podpisu do każdego słupka
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik rzucania dwoma kośćmi D8 tysiąc razy',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d8_d8.html')