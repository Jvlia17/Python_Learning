# 6.6 Ankieta. Użyj kodu znajdującego sie w programie favorite_languages.py utworzonym nieco wcześniej w tym rozdziale.

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

osoby = ['szymon', 'paweł', 'daria', 'edward']

for osoba in osoby:
    if osoba in favorite_languages.keys():
        print(f"Dziękujemy {osoba.title()} za Twoje zaangażowanie!")
    else:
        print(f"Witaj, {osoba.title()}! Zapraszamy do udziału w ankiecie.")