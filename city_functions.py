def get_city_country(city, country, population=None):
    if population:
        output = f"{city.title()}, {country.title()} - populacja {population}"
    else:
        output = f"{city.title()}, {country.title()}"
    return output