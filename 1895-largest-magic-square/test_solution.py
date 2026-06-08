import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
        self.assertEqual(self.solution.largestMagicSquare(grid), 3)

    def test_example_2(self):
        grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
        self.assertEqual(self.solution.largestMagicSquare(grid), 2)

if __name__ == '__main__':
    unittest.main()
