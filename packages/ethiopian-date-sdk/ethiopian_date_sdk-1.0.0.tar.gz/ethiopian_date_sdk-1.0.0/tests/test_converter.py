import unittest
from ethiopian_date_sdk.converter import EthiopianDateConverter

class TestEthiopianDateConverter(unittest.TestCase):

    def test_to_gregorian(self):
        self.assertEqual(EthiopianDateConverter.to_gregorian_date(2015, 1, 1), (2022, 9, 11))
        self.assertEqual(EthiopianDateConverter.to_gregorian_date(2014, 13, 5), (2022, 9, 10))

    def test_to_ethiopian(self):
        self.assertEqual(EthiopianDateConverter.to_ethiopian_date(2022, 9, 11), (2015, 1, 1))
        self.assertEqual(EthiopianDateConverter.to_ethiopian_date(2022, 9, 10), (2014, 13, 5))

if __name__ == '__main__':
    unittest.main()
