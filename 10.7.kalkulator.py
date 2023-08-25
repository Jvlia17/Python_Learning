# 10.7 Kalkulator dodawania. Kod przygotowany w ćwiczeniu 10.6 opakuj pętlą while, aby użytkownik mógł kontynuować wprowadzanie liczb nawet po popełnieniu błędu i podaniu tekstu zamiast liczby.

message = "Program do dodawania dwóch liczb\n"
message += "(Aby zakończyć działanie, wciśnij 'q')"
print(message)

while True:
    first_number = input("Pierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("Druga liczba: ")
    if second_number == 'q':
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
        answer = first_number + second_number  # answer musi być tu, bo będąc w bloku else podaje jedną z liczb jako odpowiedź, jeśli druga nie jest liczbą
    except ValueError:
        print("Któraś z podanych wartości nie jest liczbą!")
    else:
        print(answer)
