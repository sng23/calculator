import unittest
from CsvReader import CsvReader


class CsvReaderTests(unittest.TestCase):

    def setUp(self):
        self.csv_reader = CsvReader('data/Unit Test Addition.csv')

    def test_instantiate_csvreader(self):
        self.assertIsInstance(self.csv_reader, CsvReader)


if __name__ == '__main__':
    unittest.main()
