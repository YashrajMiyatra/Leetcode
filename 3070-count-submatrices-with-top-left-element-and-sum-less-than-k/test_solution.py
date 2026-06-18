import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[7,6,3],[6,6,1]]
        self.assertEqual(self.solution.countSubmatrices(grid, 18), 4)

    def test_example_2(self):
        grid = [[7,2,9],[1,5,0],[2,6,6]]
        self.assertEqual(self.solution.countSubmatrices(grid, 20), 6)

if __name__ == '__main__':
    unittest.main()
