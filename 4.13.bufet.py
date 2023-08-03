"""
# Krotka - lista, w której nie jest możliwa edycja zmiennych

wymiary = (200, 50)
# wymiary[0] = 150 wyrzuca błąd, nie można krotki edytować

wysokość = (100,) #krotka zawsze musi mieć przecinek, nawet jeśli ma jeden element

print("Stare wymiary:")
for wymiar in wymiary: # iterowanie przez krotke tak jak przez liste
    print(wymiar)

# krotki nie możemy zmienić, ale możemy stworzyć nową krotkę

wymiary = (100, 250)

print("\nNowe wymiary:")
for wymiar in wymiary: # nadpisaliśmy krotke
    print(wymiar)
"""

# 4.13 Bufet. Restauracja w stylu bufetu oferuje jedynie pięć prostych potraw. Wymień więc pięć prostych potraw i umieśc je w krotce.

proste_potrawy = ("hamburgery", "tosty", "kanapka", "rosół", "tortilla")

print("Stare menu:")
for potrawa in proste_potrawy:
    print(potrawa.title())

# proste_potrawy[2] = "pizza"

proste_potrawy = ("hamburgery", "tosty", "kanapka", "barszcz", "łazanki")

print("\nNowe menu:")
for potrawa in proste_potrawy:
    print(potrawa.title())