# 15.7 Trzy kości. Jeśli będziesz rzucać trzema kośćmi do gry typu D6, najmniejszy możliwy wynik będzie wynosić 3, natomiast największy - 18. Utwórz wizualizację pokazującą, co się stanie po rzuceniu trzema kośćmi typu D6.

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3, max_result))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1} # dtick : 1 -> nakazanie dodawania podpisu do każdego słupka
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik rzucania trzema kośćmi D6 tysiąc razy',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6_d6_d6.html')