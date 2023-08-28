"""Klasa przeznaczona do reprezentowania egzemplarza pracownika."""

class Employee():
    """Tworzy egzemplarz pracownika."""

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount