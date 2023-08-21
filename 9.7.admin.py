# 9.7 Admin. Administrator to specjalny rodzaj użytkownika. Zdefiniuj klasę o nazwie Admin dziedziczącą po klasie User utworzonej w ćwiczeniu 9.3 lub 9.5.

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

class Admin(User):
    """Tworzy egzemplarz administratora."""

    def __init__(self, first_name, last_name, age, hair_color):
        super().__init__(first_name, last_name, age, hair_color)
        self.priviliges = []

    def show_priviliges(self):
        print("Specjalne funkcje administratora:")
        for privilige in self.priviliges:
            print(f"\t- {privilige}")

admin = Admin('julia', 'rzepka', 19, 'czarny')
admin.priviliges = ['może dodac post', 'może usunąć post', 'może zbanować użytkownika']
admin.show_priviliges()