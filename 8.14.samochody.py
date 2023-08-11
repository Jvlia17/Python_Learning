# 8.14 Samochody. Utwórz funkcję przechowywującą w słowniku informacje o samochodzie.

def make_car(marka, model, **samochod):
    """Opisuje samochód."""
    samochod['marka'] = marka
    samochod['model'] = model
    return samochod

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)