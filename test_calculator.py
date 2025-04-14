# https://github.com/Fennekine14/lab10-AL-KM.git
# Partner 1: Alejandro Leyva
# Partner 2: Keon K. Moghaddam

import unittest
from calculator import add, subtract, mul, div, logarithm, exp, square_root, hypotenuse

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(5, 6), 30)

    def test_divide(self):
        self.assertEqual(div(30, 3), 10)
        self.assertEqual(div(20, 5), 4)
        self.assertEqual(div(12, 4), 3)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

if __name__ == "__main__":
    unittest.main()