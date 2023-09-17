# 16.6 Refaktoryzacja. Pętla pobierająca dane z all_eq_dicts używa zmiennych do przechowywania siły, długości i szerokości geograficznej oraz tytułu odnotowanego trzęsienia ziemi.

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Analiza struktury danych.
filename = 'data\\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

"""
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) # indent=4 nakazuje funkcji dump() sformatowanie danych z wykorzystaniem wcięć dopasowanych do struktury danych.
"""

all_eq_dicts = all_eq_data['features'] # Pobieramy dane powiązane z kluczem 'features'.

# Pobranie siły i lokalizacji trzęsień ziemi.
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Mapa trzęsień ziemi

data = [{ # Ten sposób zapisu umożliwia łatwiejsze wprowadzanie modyfikacji.
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts, # text jest wykorzystywany jako etykieta dla punktów, wyświetlana po najechaniu na nie kursorem. Etykieta zawiera informacje o sile i miejscu wystąpienia.
    'marker': { # Klucz do określania wielkości poszczególnych punktów na mapie.
        'size': [5*mag for mag in mags],
        'color': mags, # Kolor jest zdefiniowany na podstawie listy mags.
        'colorscale': 'Inferno', # Zakres kolorów do użycia.
        'reversescale': True, # True, ponieważ żółty ma być używany do najmniejszych trzęsień.
        'colorbar': {'title': 'Siła'}, # Skala kolorów.
    },
}]

my_layout = Layout(title="Trzęsienia ziemi na świecie")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')