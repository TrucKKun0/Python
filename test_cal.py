import unittest
import unit_testing

class TestCalculator(unittest.TestCase):
    def test_add(self):
        #result = unit_testing.add(3, 5)
        self.assertEqual(unit_testing.add(3, 5), 8)
        self.assertEqual(unit_testing.add(-1, 1), 0)
        self.assertEqual(unit_testing.add(-1, -1), -2)
    def test_subtract(self):
        self.assertEqual(unit_testing.subtract(10, 5), 5)
        self.assertEqual(unit_testing.subtract(-1, -1), 0)
        self.assertEqual(unit_testing.subtract(-1, 1), -2)
    def test_multiply(self):
        self.assertEqual(unit_testing.multiply(3, 5), 15)
        self.assertEqual(unit_testing.multiply(-1, 1), -1)
        self.assertEqual(unit_testing.multiply(-1, -1), 1)
    def test_divide(self): 
        self.assertEqual(unit_testing.divide(10, 2), 5)
        self.assertEqual(unit_testing.divide(-1, 1), -1)
        self.assertEqual(unit_testing.divide(-1, -1), 1)
        self.assertEqual(unit_testing.divide(5,2),2.5)
        with self.assertRaises(ValueError):
            unit_testing.divide(10, 0)
           


if __name__ == '__main__':
    unittest.main() 