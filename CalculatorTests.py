import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result(self):        
        self.assertEqual(self.calculator.result, 7)

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 5), 8)


if __name__ == '__main__':
    unittest.main()
