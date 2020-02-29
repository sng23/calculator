import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class CsvReaderTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_csvreader(self):
        self.csv_reader = CsvReader('data/Unit Test CsvReader.txt')
        self.assertIsInstance(self.csv_reader, CsvReader)
        self.assertEqual(self.csv_reader.data.__len__(), 2)

    def test_add(self):
        test_data = CsvReader('data/Unit Test Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)


if __name__ == '__main__':
    unittest.main()
