# 6.9 Ulubione miejsca. Utwórz słownik o nazwie favorite_places. Pomyśl o trzech imionach i użyj ich jako kluczy słownika.

favorite_places = {'kacper': ['zakopane', 'lublin', 'czechy'],
                   'martyna': ['leszno', 'wrocław', 'poznań'],
                   'klara': ['hiszpania', 'albania', 'rosja'],
                   }

for osoba, miejsca in favorite_places.items():
    print(f"Ulubione miejsca osoby {osoba.title()} to:")
    for miejsce in miejsca:
        print(f"\t{miejsce.title()}")