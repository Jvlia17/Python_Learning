# 8.13 Profil użytkownika. Prace rozpocznij od kopii programu user_profile.py utworzonego nieco wcześniej w tym rozdziale.

def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('julia', 'rzepka', title='inżynier', kolor_oczu='zielone', typ_włosów='kręcone')
print(user_profile)