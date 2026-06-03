import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertAlmostEqual(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]), 2.00000, places=5)

    def test_example2(self):
        s = Solution()
        self.assertAlmostEqual(s.largestTriangleArea([[1,0],[0,0],[0,1]]), 0.50000, places=5)

if __name__ == '__main__':
    unittest.main()
