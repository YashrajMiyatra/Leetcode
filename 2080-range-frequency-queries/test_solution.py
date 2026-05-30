import unittest
from solution import RangeFreqQuery

class TestSolution(unittest.TestCase):
    def test_example(self):
        rfq = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
        self.assertEqual(rfq.query(1, 2, 4), 1)
        self.assertEqual(rfq.query(0, 11, 33), 2)
        
    def test_absent_value(self):
        rfq = RangeFreqQuery([1, 2, 3])
        self.assertEqual(rfq.query(0, 2, 5), 0)
        
    def test_full_range(self):
        rfq = RangeFreqQuery([5, 5, 5, 5])
        self.assertEqual(rfq.query(0, 3, 5), 4)
        
    def test_partial_range(self):
        rfq = RangeFreqQuery([1, 2, 1, 2, 1])
        self.assertEqual(rfq.query(1, 3, 1), 1)
        self.assertEqual(rfq.query(1, 3, 2), 2)

if __name__ == '__main__':
    unittest.main()
