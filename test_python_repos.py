import unittest
from python_repos import get_python_repos


class NamesTestCase(unittest.TestCase):
    """Testy dla programu python_repos.py"""

    def test_python_repos(self):
        status_code = get_python_repos()
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()
