# 5.10. Sprawdzenie nazw użytkowników. Wykonaj działania w celu utworzenia programu symulującego sposób, w jaki witryna internetowa gwarantuje, że każdy użytkownik będzie miał unikalną nazwę.

current_users = ['hipo14', 'tiger64', 'mimi', 'hana8', 'vlad']
new_users = ['Vlad', 'pokkie', 'tris78']

'''
current_users_lower = [] # musimy, aby traktować użytkowników Vlad i vlad jako jednego
for user in current_users:
    current_users_lower.append(user.lower())
'''

current_users_lower = [user.lower() for user in current_users]
# mega mądra i szybka opcja

for user in new_users:
    if user.lower() not in current_users_lower:
        print(f'Nazwa {user} jest wolna i możesz jej użyć')
    else:
        print(f'Nazwa {user} jest zajęta. Wybierz inna nazwę.')
