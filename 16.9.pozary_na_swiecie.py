# 16.9 Pożary na świecie. W materiałach przygotowanych dla tego rozdziału znajduje się plik o nazwie world_fires_1_day.csv.

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import csv

# Analiza struktury danych.
filename = 'data\\world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Do odczytu które indeksy mają znaczące dla nas informacje
    for index, column_header in enumerate(header_row): # Enumerate -> pobiera indeksy i wartości poszczególnych elementów.
        print(index, column_header)


    lats, lons, brightnesses = [], [], []

    for row in reader:

        lat = int(float(row[0]))
        lon = int(float(row[1]))
        brightness = int(float(row[2]))

        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)

# Mapa trzęsień ziemi

data = [{ # Ten sposób zapisu umożliwia łatwiejsze wprowadzanie modyfikacji.
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': { # Klucz do określania wielkości poszczególnych punktów na mapie.
        'size': 5,
        'color': brightnesses, # Kolor jest zdefiniowany na podstawie listy mags.
        'colorscale': 'Inferno', # Zakres kolorów do użycia.
        'reversescale': True, # True, ponieważ żółty ma być używany do najmniejszych trzęsień.
        'colorbar': {'title': 'Siła'}, # Skala kolorów.
    },
}]

my_layout = Layout(title="Siła pożarów")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')