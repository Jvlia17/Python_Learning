'''
# Przekazywanie argumentów może się odbywać na 3 sposoby:
# 1. Argumenty pozycyjne - ułożone w takiej samej kolejności, jak parametry
# 2. Argumenty w postaci słów kluczowych - argument składa się z nazwy zmiennej i wartości
# 3. Listy i słowniki wartości.

# Argumenty pozycyjne:

def describe_pet(animal_type, pet_name):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

describe_pet('chomik', 'harry')
describe_pet('pies', 'willie') # kolejność ma znaczenie, jeśli byśmy napisali ('willie', 'pies') to byśmy otrzymali zwierzę williego i imieniu Pies

# Argumenty w postaci słów kluczowych:

def describe_pet(animal_type, pet_name):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

describe_pet(animal_type='chomik', pet_name='harry') # nie ma obowiązku przejmowania się kolejnością argumentów
describe_pet(pet_name='willie', animal_type='pies') # tutaj zamiana kolejności - program nadal dobrze dopasowuje argumenty do parametrów

# Wartości domyślne

def describe_pet(pet_name, animal_type='pies'): # Została tutaj używa wartość domyślna. Jeśli większość naszych zwierząt to psy, to warto coś takiego zastosować. Jeśli jednak zostanie podany argument zastępujący 'pies' to zostanie on użyty zamiast wartości domyślnej.
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

describe_pet('harry')
# Ważne -> gdybyśmy mieli najpierw (animal_type = 'pies', pet_name) i argument ('harry'), program nadal stosuje argumenty pozycyjne, więc zostaje zastąpiona wartość animal_type, a nie pet_name, przez co trzeba zmienić kolejność LUB użyć argumentów w postaci słów kluczowych
# W skrócie - definicje na końcu

# Tak więc mamy różne sposoby wywołania tej samej funkcji:

def describe_pet(pet_name, animal_type='pies'):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

describe_pet('harry')
describe_pet(pet_name='harry', animal_type='pies')

describe_pet('william', 'chomik')
describe_pet(pet_name='william', animal_type='chomik')
describe_pet(animal_type='chomik', pet_name='william')

# jeśli funkcja generuje te same dane wyjściowe, to najlepiej wybrać tą, która jest najłatwiejsza do zrozumienia
'''

# 8.3 T-shirt. Utwórz funkcję o nazwie make_shirt(), akceptująca wielkość koszulki oraz tekst, który ma zostać na niej nadrukowany.

def make_shirt(size, text):
    """Wypisuje rozmiar i tekst na koszulce."""
    print(f"Zamówiłeś koszulkę w rozmiarze {size.upper()} z tekstem: '{text}'.")

make_shirt('xs', "I love capybaras") # argumenty pozycyjne
make_shirt(size='l', text="made in china") # argumenty w postaci słów kluczowych