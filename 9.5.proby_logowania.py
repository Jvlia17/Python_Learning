# 9.5 Próby logowania. Pracę rozpocznij od programu utworzonego w ćwiczeniu 9.3. Do klasy User dodaj metodę o nazwie increment_login_attempts(), pozwalający na inkrementację wartości login_attempts o 1.

class User():
    """Tworzy egzemplarz użytkownika."""

    def __init__(self, first_name, last_name, age, hair_color):
         """Inicjalizacja atrybutów first_name i last_name."""
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
         self.hair_color = hair_color
         self.login_attempts = 0

    def describe_user(self):
        """Opisuje użytkownika."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Użytkownik {full_name.title()} ma {self.age} lat i {self.hair_color} kolor włosów.")

    def greet_user(self):
        """Powitanie użytkownika."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Witaj, {full_name.title()}!")

    def increment_login_attempts(self):
        """Pozwala na inkrementację wartości login_attempts o 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Pozwala na zerowanie wartości login_attempts"""
        self.login_attempts = 0

user = User('julia', 'rzepka', '21', 'czarny')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Użytkownik {user.first_name.title()} tyle razy próbował wpisać hasło: {user.login_attempts}")
user.reset_login_attempts()
print(f"Użytkownik {user.first_name.title()} tyle razy próbował wpisać hasło: {user.login_attempts}.")