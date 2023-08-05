# 6.8 Zwierzęta. Utwórz kilka słowników i nadaj im nazwy zwierząt.

pies = {'gatunek': 'pies', 'właściciel': 'Kacper'}
kot = {'gatunek': 'kot', 'właściciel': 'Martyna'}
szczur = {'gatunek': 'szczur', 'właściciel': 'Maurycy'}

pets = [pies, kot, szczur]

for pet in pets:
    print(f"Właścicielem zwierzęcia {pet['gatunek']} jest {pet['właściciel']}")