'''
alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'żółty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
# 3 słowniki umieszczone w liście

for alien in aliens:
    print(alien)
'''

aliens = []

# Utworzenie 30 zielonych obcych
for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien)

# Wyświetlenie pierwszych pięciu obcych
for alien in aliens[:5]:
    print(alien)
print('...')

# Wyświetlenie całkowitej liczby utworzonych obcych
print(f"Całkowita liczba obcych: {len(aliens)}")

# pierwsi 3 obcy: na zolto , srednia, 10 pkt

for alien in aliens[:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['points'] = 10
        alien['speed'] = 'średnio'
    elif alien['color'] == 'żółty':
        alien['color'] = 'czerwony'
        alien['points'] = 15
        alien['speed'] = 'szybko'

for alien in aliens[:5]:
    print(alien)