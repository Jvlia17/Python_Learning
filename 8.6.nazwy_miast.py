'''
def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# return -> pobiera wartość z wewnątrz funkcji i przekazuje ją do wiersza kodu, w którym wystąpiło wywołanie tej funkcji

# dodanie argumentu opcjonalnego
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Zwraca elegancko sformatowane pełne imię i nazwisko."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker') # należy pamiętać, że drugie imię musi iśc jako ostatnie, przez kolejność parametrów
print(musician)
# przypisaliśmy parametrowi middle_name domyślną wartość w postaci pustego ciągu tekstowego. Następnie przy pomocy if sprawdzamy czy ten argument występuje i wykonujemy odpowiednią funkcję.
# wartość '' jest traktowana jako pusty ciąg tekstowy i zwraca False

def build_person(first_name, last_name, age = None): # None dla wartości liczbowych, '' dla wartości tekstowych
    """Zwraca słownik informacji o danej osobie"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 30)
print(musician)

def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True: # działa w nieskończoność
    print("\nProszę podac imię i nazwisko:")
    print("(wpisz 'q', aby zakończyć pracę w dowolnym momencie)")

    f_name = input("Imię: ")
    if f_name == 'q':
        break

    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Witaj, {formatted_name}!")
# w powyższej pętli umożliwiliśmy wyjście w dowolnym momencie działania programu
'''

# 8.6 Nazwy miast. Utwórz funkcję o nazwie city_country() pobierającą nazwę miasta i kraju, w którym ono leży. Wartością zwrotną funkcji powinien być ciąg tekstowy sformatowany w dany sposób.

def city_coutry(city, country):
    """Zwraca ciąg tekstowy"""
    print(f"{city.title()}, {country.title()}")

city_coutry('wrocław', 'poland')