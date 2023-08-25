# 10.9 Ciche koty i psy. Blok except w programie utworzonym w poprzednim ćeiczeniu zmodyfikuj w taki sposób, aby brak pliku powodował jedynie ciche niepowodzenie.

file_paths = {"pliki_tekstowe/cats.txt": "cats", "pliki_tekstowe/dogs.txt": "dogs", "pliki_tekstowe/rodents.txt": "rodents"} # Użyłam słownika, aby móc na końcu wypisać jakie imiona wypisuję -> kotów czy psów.

for file_path in file_paths:
    try:
        with open(file_path, 'r', encoding = 'utf-8') as f:
            names = f.read()
    except FileNotFoundError:
        pass # ciche niepowodzenie
    else:
        print(f"{file_paths[file_path].title()} names: {names}")
