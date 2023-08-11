# 8.5 Miasta. Utwórz funkcję o nazwie describe_city, akceptującą nazwę miasta i kraju.

def describe_city(city, country='Polsce'):
    """Wypisuje proste zdanie o miastach."""
    print(f"{city.title()} leży w {country.title()}")

describe_city('leszno')
describe_city('praga', 'czechach')
describe_city('wrocław')