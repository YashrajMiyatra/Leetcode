import unittest
from solution import MedianFinder

class TestMedianFinder(unittest.TestCase):
    def test_example_1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)

if __name__ == '__main__':
    unittest.main()
