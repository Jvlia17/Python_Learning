# 5.6 Etapy życia. Przygotuj konstrukcję if-else ustalającą etap życia danej osoby. Przypisz wartośc zmiennej age.

age = 80

if age < 2:
    print("Jesteś niemowlęciem.")
elif age < 4:
    print("Jesteś dzieckiem, które uczy się chodzić.")
elif age < 13:
    print("Jesteś dzieckiem.")
elif age < 20:
    print("Jesteś nastolatkiem.")
elif age < 65:
    print("Jestes dorosły.")
else:
    print("Jesteś seniorem.")