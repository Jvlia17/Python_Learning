'''

# (*toppings) tworzy pustą krotkę o nazwie toppings i umieszczenie na niej podanych wartości (dowolna ich ilość)
# Ważne! (*toppings) musi być na końcu parametrów!
# Często używa się po prostu *args

def make_pizza(size, *toppings):
    """Wyświetlanie listy dodatków wybranych przez klienta."""
    print(f"\nPrzygotowuje pizzę o wielkości {size}cm z następującymi dodatkami: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(40, 'pepperoni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# **user_info -> tworzy pusty słownik i umieszcza do niego wszystkie otrzymacze klucze-wartości
# często używa się **kwargs -> klucz-wartość argumenty
def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='fizyka')
print(user_profile)
'''

# 8.12 Kanapki. Utwórz funkcję akceptującą listę składników, które klient chce umieścić w zamawianej kanapce.

def make_sandwich(*ingredients):
    """Podsumowuje zamówienie klienta."""
    print(f"\nZamówiłeś kanapkę z:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('jajkiem')
make_sandwich('szynką', 'boczkiem')
make_sandwich('serem', 'szynką', 'pomidorem')