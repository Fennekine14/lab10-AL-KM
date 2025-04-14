import unittest
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,4),5)
        self.assertEqual(add(6,10),16)
        self.assertEqual(add(100,5),105)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(16,12),4)
        self.assertEqual(sub(0,-4),4)
        self.assertEqual(sub(-1,3),-4)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5,0)
        with self.assertRaises(ZeroDivisionError):
            div (100,0)
        with self.assertRaises(ZeroDivisionError):
            div(-2,0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10,1)
        with self.assertRaises(ValueError):
            log(20,-5)
        with self.assertRaises(ValueError):
            log(100,0)
        with self.assertRaises(ValueError):
            log(2,-10)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
