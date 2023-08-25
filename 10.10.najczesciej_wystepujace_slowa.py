# 10.10 Najczęściej występujące słowa. Odwiedź witrynę projektu Gutenberg i wybierz kilka innych książek, które chciałbyś przeanalizować.

file_path = "pliki_tekstowe/gorale.txt"

with open(file_path, 'r', encoding = 'utf-8') as f:
    text = f.read()

print(text.lower().count('za')) # Liczymy ile razy występuje słowo 'za' w pliku tekstowym
# Użyliśmy funkcji .lower(), aby każde 'Za' też traktowac jako 'za'