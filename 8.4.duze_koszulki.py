# 8.4 Duże koszulki. Zmodyfikuj funkcję make_shirt() tak, aby domyślnie były przygotowywane duże koszulki z nadrukowanym tekstem "Uwielbiam Pythona".

def make_shirt(size='l', text="Kocham Pythona"):
    """Wypisuje rozmiar i tekst na koszulce."""
    print(f"Zamówiłeś koszulkę w rozmiarze {size.upper()} z tekstem: '{text}'.")

make_shirt() # koszulka z wartościami domyślnymi
make_shirt('m')
make_shirt('s', 'I love capybaras')