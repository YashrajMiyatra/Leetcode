import unittest
from solution import StockPrice

class TestStockPrice(unittest.TestCase):
    def test_example_1(self):
        obj = StockPrice()
        obj.update(1, 10)
        obj.update(2, 5)
        self.assertEqual(obj.current(), 5)
        self.assertEqual(obj.maximum(), 10)
        obj.update(1, 3)
        self.assertEqual(obj.maximum(), 5)
        obj.update(4, 2)
        self.assertEqual(obj.minimum(), 2)

if __name__ == '__main__':
    unittest.main()
