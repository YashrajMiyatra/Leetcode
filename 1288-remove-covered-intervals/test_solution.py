import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.removeCoveredIntervals([[1,4],[3,6],[2,8]]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.removeCoveredIntervals([[1,4],[2,3]]), 1)

if __name__ == '__main__':
    unittest.main()
