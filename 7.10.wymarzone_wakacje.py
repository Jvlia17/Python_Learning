# 7.10 Wymarzone wakacje. Przygotuj program pytający użytkowników o ich wymarzone wakacje.

dream_holidays = {}
polling_active = True

while polling_active:
    name = input("Jak masz na imię? ")
    place = input("Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał? ")
    dream_holidays[name] = place # ważna konstrukcja, bez append! Słowniki nie mają funkcji .append()
    finish = input("Czy chcesz już skończyć ankietę? (tak / nie) ")

    if finish == 'tak':
        polling_active = False

for name, place in dream_holidays.items():
    print(f"Osoba {name} marzy o wakacjach w miejscu o nazwie {place}")