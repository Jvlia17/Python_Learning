# 10.4 Księga gości. Utwórz pętlę while, w której każdy użytkownik będzie musiał podac swoje imię.

file_path = 'pliki_tekstowe/guest_book.txt'
name = []
while True:
    message = f"Jeśli chcesz zakończyć, wciśnij 'q'\n"
    message += f"Jak masz na imię? "
    name = input(message)
    
    if name == 'q':
        break
    else:
        print(f"Witaj, {name.title()}\n")
        with open(file_path, 'a') as file_object:
            file_object.write(f"Ta osoba odwiedziła Twoją stronę: {name.title()}\n")