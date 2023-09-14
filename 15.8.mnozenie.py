# 15.8 Mnożenie. Kiedy rzucasz dwiema kośćmi do gry, z reguły dodajesz dwie liczby, aby otrzymac wynik. Utwórz wizualizację pokazującą co się stanie, jeśli zamiast dodać obie liczby, pomnożysz je.

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = [die.roll()*die.roll() for roll_num in range(1000)]

max_result = die.num_sides * die.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

x_values = list(range(1, max_result))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1} # dtick : 1 -> nakazanie dodawania podpisu do każdego słupka
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik pomnożenia wyniku rzucania dwoma kośćmi D6 tysiąc razy',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d8_d8.html')