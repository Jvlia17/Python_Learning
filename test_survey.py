import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase): # klasa TestAnonymousSurvey dziedziczy po klasie unittest.TestCase
    """Testy dla klasy AnonymousSurvey."""

    def setUp(self):
        """Utworzenie ankiety i zestawu odpowiedzi do użycia we wszystkich metodach testowych."""
        question = "Jaki jest Twój ojczysty język?"
        self.my_survey = AnonymousSurvey(question) # utworzenie egzemplarza ankiety
        self.responses = ['angielski', 'hiszpański', 'polski'] # przygotowanie listy odpowiedzi

# Ważne! Prefiks 'self' pozwala na użycie w dowolnym miejscu klasy.
# Dzięki stworzeniu metody setUp() dwie poniższe metody nie muszą tworzyć własnych obiektów.
# Takie podejście jest łatwiejsze niż tworzenie nowego zestawu egzemplarzy i atrybutów dla każdej metody testowej.

    def test_store_single_response(self):
        """Sprawdzanie, czy pojedyncza odpowiedź jest prawidłowo przechowywana."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses) # Sprawdzamy, czy wśród my_survey.responses znajduje się odpowiedz 'angielski'

    def test_store_three_responses(self):
        """Sprawdzenie, czy trzy pojedyncze odpowiedzi są prawidłowo przechowywane."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses) # wykonujemy metodę asercji dla każdego elementu przechowywanego teraz w liście my_survey.responses

if __name__ == '__main__':
    unittest.main()