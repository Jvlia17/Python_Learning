# 6.5 Rzeki. Utwórz słownik zawierający trzy ważne rzeki oraz kraje, przez które one płyną.

rzeki = {'dunaj': 'niemcy',
         'odra': 'polska',
         'nil': 'egipt',
         }

for rzeka, kraj in rzeki.items():
    print(f"{rzeka.title()} przepływa przez {kraj.title()}.")

print("\nWszystkie rzeki w słowniku to:")
for rzeka in rzeki.keys():
    print(rzeka.title())

print("\nWszystkie państwa w słowniku to:")
for kraj in rzeki.values():
    print(kraj.title())