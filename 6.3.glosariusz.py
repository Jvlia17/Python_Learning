# 6.3 Glosariusz. Słownik Pythona można wykorzystać do przygotowania rzeczywistego słownika. Jednak w celu uniknięcia niejasności nazwiemy go glosariuszem.

glosariusz = {'PEP 8': 'Zbiór informacji o poprawnym i czytelnym pisaniu kodu',
              'krotka': 'lista z niezmieniającymi się elementami',
              'słownik': 'zbiór par kluczy - wartości',
              'elif': 'następuje po if i przed else',
              'nahida': 'postać, którą źle zbudowaliśmy',
              }

for słowo in glosariusz:
    print(f"Znaczenie słowa {słowo} to: {glosariusz[słowo]}.\n")