# 9.3 Użytkownicy. Przygotuj klasę o nazwie User.

class User():
    """Tworzy egzemplarz użytkownika."""

    def __init__(self, first_name, last_name, age, hair_color):
         """Inicjalizacja atrybutów first_name i last_name."""
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
         self.hair_color = hair_color

    def describe_user(self):
        """Opisuje użytkownika."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Użytkownik {full_name.title()} ma {self.age} lat i {self.hair_color} kolor włosów.")

    def greet_user(self):
        """Powitanie użytkownika."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Witaj, {full_name.title()}!")

user_1 = User('kacper', 'nowak', 21, 'brązowy')
user_2 = User('karolina', 'pasieka', 15, 'blond')
user_3 = User('julia', 'rzepka', 23, 'czarny')

users = [user_1, user_2, user_3]
for user in users:
    user.describe_user()
    user.greet_user()
    print("\n")