import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.minTimeToVisitAllPoints([[3,2],[-2,2]]), 5)

if __name__ == '__main__':
    unittest.main()
