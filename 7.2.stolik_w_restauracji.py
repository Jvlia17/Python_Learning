# 7.2 Stolik w restauracji. Utwórz program pytający klienta, na ile osób chce zarezerwować stolik. Jeżeli odpowiedzią jest liczba większa niż 8, powinienes wyświetlić komunikat o konieczności zaczekania na stolik.

how_big = input("Dzień dobry! Na ile osób chciałbyś zarezerwować stolik? ")
how_big = int(how_big)

if how_big > 8:
    print("Niestety będziesz musiał zaczekać.")
else:
    print("Stolik jest gotowy.")