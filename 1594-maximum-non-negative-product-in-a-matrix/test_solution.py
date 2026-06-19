import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
        self.assertEqual(self.solution.maxProductPath(grid), -1)

    def test_example_2(self):
        grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
        self.assertEqual(self.solution.maxProductPath(grid), 8)

    def test_example_3(self):
        grid = [[1,3],[0,-4]]
        self.assertEqual(self.solution.maxProductPath(grid), 0)

if __name__ == '__main__':
    unittest.main()
