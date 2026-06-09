import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[1,3,3],[2,5,4],[4,3,5]]
        k = 2
        self.assertEqual(self.solution.minimumCost(grid, k), 7)

    def test_example_2(self):
        grid = [[1,2],[2,3],[3,4]]
        k = 1
        self.assertEqual(self.solution.minimumCost(grid, k), 9)

if __name__ == '__main__':
    unittest.main()
