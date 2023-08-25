# 10.8 Koty i psy. Utwórz dwa pliki o nazwach cats.txt i dogs.txt. W pierwszym pliku umieść przynajmniej trzy imiona kotów, natomiast w drugim przynajmniej trzyimiona psów.

file_paths = {"pliki_tekstowe/cats.txt": "cats", "pliki_tekstowe/dogs.txt": "dogs", "pliki_tekstowe/rodents.txt": "rodents"} # Użyłam słownika, aby móc na końcu wypisać jakie imiona wypisuję -> kotów czy psów.

for file_path in file_paths:
    try:
        with open(file_path, 'r', encoding = 'utf-8') as f:
            names = f.read()
    except FileNotFoundError:
        print(f"Plik {file_path} nie został odnaleziony!")
    else:
        print(f"{file_paths[file_path].title()} names: {names}")
