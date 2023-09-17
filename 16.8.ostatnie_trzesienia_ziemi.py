# 16.8. Ostatnie trzęsienia ziemi. W internecie możesz znaleźć pliki danych zawierające informacje o trzęsieniach ziemi odnotowanych w ciągu ostatniej godziny, ostatniego dnia oraz ostatnich 7 i 30 dni.

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Analiza struktury danych.
filename = 'data\\all_day.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

"""
readable_file = 'data/readable_all_day.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) # indent=4 nakazuje funkcji dump() sformatowanie danych z wykorzystaniem wcięć dopasowanych do struktury danych.
"""

all_eq_dicts = all_eq_data['features'] # Pobieramy dane powiązane z kluczem 'features'.
graph_title = all_eq_data['metadata']['title']
print(graph_title)

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

my_layout = Layout(title=graph_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')