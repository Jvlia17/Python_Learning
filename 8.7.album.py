# 8.7 Album. Utwórz funkcję o nazwie make_album() odpowiedzialną za zbudowanie słownika reprezentującego album muzyczny.

def make_album(band_name, album_name, number_of_tracks = None):
    """Zwraca album muzyczny."""
    album = {'band/artist': band_name, 'album': album_name}
    if number_of_tracks:
        album['number of tracks'] = number_of_tracks
    return album

Arctic_Monkeys = make_album('Arctic Monkeys', 'Favorite worst nightmare', 12)
Melanie_Martinez = make_album('Melanie Martinez', 'K-12')
Julia_Rzepka = make_album('Julia Rzepka', 'No idea')

print(Arctic_Monkeys)
print(Melanie_Martinez)
print(Julia_Rzepka)