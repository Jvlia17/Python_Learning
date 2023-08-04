'''
user_0 = {
    'username': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski',
}
# k -> key, v -> value
# .items() -> zwraca liste par klucz-wartość

for k, v in user_0.items():
    print(f"\nKlucz: {k}")
    print(f"Wartość: {v}")

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

friends = ['sara', 'janek']

for name, language in favorite_languages.items():
    print(f"Witaj, {name.title()}")

    if name in friends:
        print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem programowania jest {language.title()}")

# .keys() -> do odszukania konkretnego klucza, bez iterowania przez wszystkie elementy słownika
if 'elżbieta' not in favorite_languages.keys():
    print(f"\nElżbieta, proszę, weź udział w naszej ankiecie!")

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, dziękujemy za udział w ankiecie!")

# .values() -> do odszukania konkretnej wartości
print(f"\nW ankiecie zostały wymienione następujące języki programowania: ")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")

# set() -> Python tworzy zbiory z listy, dzięki czemu elementy sie nie powtarzają
# Zbiór można stworzyć samodzielnie w taki sposób:

zbiór = {'python', 'c', 'c', 'python', 'ruby'}
print(zbiór)

# [element] -> lista
# (element, element) -> krotka
# {klucz: wartość} -> słownik
# {element, element} -> zbiór
'''

# 6.4 Glosariusz 2. Skoro już wiesz, jak można przeprowadzić iterację przez słownik, to zmodyfikuj kod ćwiczenia 6.3 z wczesniejszej części rozdziału.

glosariusz = {'PEP 8': 'Zbiór informacji o poprawnym i czytelnym pisaniu kodu',
              'krotka': 'lista z niezmieniającymi się elementami',
              'słownik': 'zbiór par kluczy - wartości',
              'elif': 'następuje po if i przed else',
              'nahida': 'postać, którą źle zbudowaliśmy',
              'glosariusz': 'słownik objaśniający wyrazy trudniejsze'
              }

# Pamiętaj o .items()
for słowo, znaczenie in glosariusz.items():
    print(f"Znaczenie słowa {słowo} to: {znaczenie}.\n")