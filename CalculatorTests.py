import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 7)


if __name__ == '__main__':
    unittest.main()
