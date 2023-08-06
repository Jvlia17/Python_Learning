# 7.5 Bilety do kina. Cena biletu do kina jest uzależniona od wieku widza.

# 1. break
while True:
    promt = "Jeśli chcesz skończyć, wpisz 'koniec'"
    promt += "\nIle masz lat? "
    age = input(promt)

    if age != 'koniec':
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print(f"Bilet będzie kosztował {price} złotych.\n")
    else:
        break