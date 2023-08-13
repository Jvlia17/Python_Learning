# 8.8 Albumy użytkowników. Pracę rozpocznij od programu utworzonego w ćwiczeniu 8.7. Dodaj pętlę while pozwalającą użytkownikom na wprowadzanie artysty i tytułu płyty.

def make_album(band_name, album_name, number_of_tracks=None):
    """Zwraca album muzyczny."""
    album = {'band/artist': band_name, 'album': album_name}
    if number_of_tracks:
        album['number of tracks'] = number_of_tracks
    return album

while True:
    print("\nStworzę album z podanego artysty i tytułu płyty.")
    print("(jeśli chcesz zakończyć, naciśnij 'q')")
    band_name = input("Nazwa zespołu lub artysty: ")
    if band_name == 'q':
        break
    album_name = input("Nazwa albumu: ")
    if album_name == 'q':
        break
    album = make_album(band_name=band_name, album_name=album_name)
    print(f"Twój album: {album}")