# 10.2 Poznajemy C. Metodę replace() można wykorzystać do zastąpienia dowolnego słowa w ciągu tekstowym zupełnie innym słowem.

filename = 'pliki_tekstowe/learning_python.txt'

with open(filename) as file_object: # Poprzez umieszczenie wierszy na liście.
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Pythonie', 'C').strip())

# Uwaga! Metoda .replace() nie zamienia na stałe, więc albo trzeba od razu wyświetlić, albo zapisać jako zmodyfikowany tekst.