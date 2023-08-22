# 9.15 Analiza loterii. Wykorzystaj pętlę do ustalenia, jak trudno jest wygrac w loterii, którą modelowałes w poprzednim ćwiczeniu.
from random import choice

list = ['a', 2, 'c', 5, 'o', 1, 'p', 6, 'j', 7, 3, 0, 4, 8, 9]
my_ticket = [2, 5, 'a', 1]
winning_coupon = []
iterations = 0

while my_ticket != winning_coupon:
    winning_coupon = [choice(list), choice(list), choice(list), choice(list)]
    print(winning_coupon)
    iterations += 1

print(f"Po tylu losowaniach kupon wygrał: {iterations}")