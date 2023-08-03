# 2.7 Usunięcie białych znaków z imienia. Zapisz w zmiennej imię osoby wraz z pewnymi białymi znakami na początkui końcu imienia. Upewnij się, że co najmniej raz użyłeś sekwencji \t i \n.
# Wyświetl to imię wraz ze znakami odstępu. Następnie wyświetl je jeszcze trzy razy, ale za każdym razem wykorzystaj jedną z metod przeznaczonych do usuwania białych znaków: lstrip(), rstrip() i strip().

zmienna = "\tjulia\n"

print(zmienna.title())
print((zmienna.title()).lstrip())
print((zmienna.title()).rstrip())
print((zmienna.title()).strip())