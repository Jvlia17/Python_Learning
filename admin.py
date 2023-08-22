"""Klasa przeznaczona do zaprezentowania administratora."""
from user import User


class Priviliges():
    def __init__(self):
        self.priviliges = ['może dodac post', 'może usunąć post',
                           'może zbanować użytkownika']

    def show_priviliges(self):
        print("Specjalne funkcje administratora:")
        for privilige in self.priviliges:
            print(f"\t- {privilige}")


class Admin(User):
    """Tworzy egzemplarz administratora."""

    def __init__(self, first_name, last_name, age, hair_color):
        super().__init__(first_name, last_name, age, hair_color)
        self.priviliges = Priviliges()
