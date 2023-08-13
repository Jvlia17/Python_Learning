'''
# 1. Importujemy plik pizza.py. Pliki muszą być w tym samym katalogu. Moduł pizza.py udostępnia swoją funkcję make_pizza().
import pizza

pizza.make_pizza(40, 'pepperoni')
pizza.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# 2. możemy też zaimportowac wybraną funkcję, zamiast całego modułu
from pizza import make_pizza

make_pizza(40, 'pepperoni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# 3. wybraną funkcję możemy zaimportować i zmienić jej alias (bo np. jest za długa lub koliduje z inną nazwą)
from pizza import make_pizza as mp

mp(40, 'pepperoni')
mp(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# 4. możemy tez nadać alias dla całego modułu
import pizza as p

p.make_pizza(40, 'pepperoni')
p.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# 5. Możemy też za pomocą * zaimportować wszystkie funkcje z modułu, jednakże nie jest to super polecana opcja, ponieważ funkcje mogą kolidowac z innymi

from pizza import *

make_pizza(40, 'pepperoni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

# Kwestie estetyczne -> przy podawaniu wartości domyślnych parametrów nie ma spacji między znakiem równości parametr'wartość_domyślna'
# Przy wywołaniu funkcji ze słowami kluczowymi tak samo bez spacji nazwa_funkcji(parametr1='wartość)
'''

# 8.15 Wydruk modeli. Funkcje z programu print_models.py umieść w oddzielnym pliku o nazwie printing_functions.py.

from printing_functions import print_models as pm, show_completed_models as scm
# import printing_functions
# import printing_functions as pf
# from printing_functions import *
# grom printing_functions import print_models, show_completed_models

unprinted_designs = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)