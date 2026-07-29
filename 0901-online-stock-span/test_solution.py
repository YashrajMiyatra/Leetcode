import unittest
from solution import StockSpanner

class TestStockSpanner(unittest.TestCase):
    def test_example_1(self):
        spanner = StockSpanner()
        self.assertEqual(spanner.next(100), 1)
        self.assertEqual(spanner.next(80), 1)
        self.assertEqual(spanner.next(60), 1)
        self.assertEqual(spanner.next(70), 2)
        self.assertEqual(spanner.next(60), 1)
        self.assertEqual(spanner.next(75), 4)
        self.assertEqual(spanner.next(85), 6)

if __name__ == '__main__':
    unittest.main()
