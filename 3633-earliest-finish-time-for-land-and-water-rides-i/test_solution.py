import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.earliestFinishTime([2,8], [4,1], [6], [3]), 9)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.earliestFinishTime([5], [3], [1], [10]), 14)
        
    def test_single_element(self):
        s = Solution()
        self.assertEqual(s.earliestFinishTime([1], [1], [1], [1]), 3)

if __name__ == '__main__':
    unittest.main()
