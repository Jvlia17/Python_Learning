def make_pizza(size, *toppings):
    """Podsumowywuje informacje o przygotowywanej pizzy."""
    print(f"\nPrzygotowuję pizzę o wielkości {size}cm z następującymi dodatkami:")
    for topping in toppings:
        print(f"- {topping}")