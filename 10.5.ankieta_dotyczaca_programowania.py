# 10.5 Ankieta dotycząca programowania. Utwórz pętlę while, w której użytkownicy będą musieli udzielić odpowiedzi na pytanie ,,Dlaczego lubisz programowanie?"

file_path = 'pliki_tekstowe/answers.txt'
answer = []
while True:
    message = f"\nJeśli chcesz zakończyć, wciśnij 'q'\n"
    message += f"Dlaczego lubisz programowanie? "
    answer = input(message)
    if answer == 'q':
        break
    else:
        with open(file_path, 'a') as file_object:
            file_object.write(f"{answer}\n")
