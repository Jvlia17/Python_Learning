# 9.14 Loteria. Utwórz listę lub krotkę zawierającą serię dziesięciu liczb i pięciu liter.
from random import choice

list = ['a', 2, 'c', 5, 'o', 1, 'p', 6, 'j', 7, 3, 0, 4, 8, 9]
winning_coupon = f"{choice(list)}{choice(list)}{choice(list)}{choice(list)}"
print(f"Kupon o numerze: {winning_coupon} wygrywa nagrodę! Zapraszamy po odbiór nagrody.")