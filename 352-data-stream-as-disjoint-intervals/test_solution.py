import unittest
from solution import SummaryRanges

class TestSolution(unittest.TestCase):
    def test_example(self):
        obj = SummaryRanges()
        obj.addNum(1)
        self.assertEqual(obj.getIntervals(), [[1, 1]])
        
        obj.addNum(3)
        self.assertEqual(obj.getIntervals(), [[1, 1], [3, 3]])
        
        obj.addNum(7)
        self.assertEqual(obj.getIntervals(), [[1, 1], [3, 3], [7, 7]])
        
        obj.addNum(2)
        self.assertEqual(obj.getIntervals(), [[1, 3], [7, 7]])
        
        obj.addNum(6)
        self.assertEqual(obj.getIntervals(), [[1, 3], [6, 7]])

if __name__ == '__main__':
    unittest.main()
