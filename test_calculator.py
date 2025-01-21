import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_odejmowanie(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_mnożenie(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()
