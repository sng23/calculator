import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result(self):        
        self.assertEqual(self.calculator.result, 0)

    def test_add(self):
        result = 8
        self.assertEqual(self.calculator.add(3, 5), result)
        self.assertEqual(self.calculator.result, result)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 5), -2)
        self.assertEqual(self.calculator.result, -2)


if __name__ == '__main__':
    unittest.main()
