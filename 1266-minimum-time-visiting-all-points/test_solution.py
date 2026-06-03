import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]), 7)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.minTimeToVisitAllPoints([[3,2],[-2,2]]), 5)

    def test_single_point(self):
        s = Solution()
        self.assertEqual(s.minTimeToVisitAllPoints([[0,0]]), 0)

if __name__ == '__main__':
    unittest.main()
