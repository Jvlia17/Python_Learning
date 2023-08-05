# 6.11 Miasta. Utwórz słownik o nazwie cities. Jako klucze podaj nazwy trzech miast. Dla każdego z nich utwórz oddzielny słownik zawierający informacje o danym mieście.

cities = {
    'Wrocław': {
    'country': 'Polska',
    'population': '638 659',
    'fact': 'super cool ekstra klasa',
    },

    'Gdańsk': {
        'country' : 'Poland',
        'population': '582 205',
        'fact': 'może być',
    },

    'Praga': {
        'country': 'Czechy',
        'population': '1 309 000',
        'fact': 'smażony syr',
    },
}

for city, info in cities.items():
    print(f"Nazwa miasta: {city}")
    kraj = f"{info['country']}"
    populacja = f"{info['population']}"
    fakt = f"{info['fact']}"
    print(f"\tKraj: {kraj}, populacja: {populacja}, fakt: {fakt}")

# Ważna konstrukcja kraj = f"{info['country']}"