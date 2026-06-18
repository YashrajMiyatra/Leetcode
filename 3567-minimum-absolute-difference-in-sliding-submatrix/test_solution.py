import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[1,8],[3,-2]]
        self.assertEqual(self.solution.minAbsoluteDifference(grid, 2), [[2]])

    def test_example_2(self):
        grid = [[3,-1]]
        self.assertEqual(self.solution.minAbsoluteDifference(grid, 1), [[0, 0]])

    def test_example_3(self):
        grid = [[1,-2,3],[2,3,5]]
        self.assertEqual(self.solution.minAbsoluteDifference(grid, 2), [[1, 2]])

if __name__ == '__main__':
    unittest.main()
