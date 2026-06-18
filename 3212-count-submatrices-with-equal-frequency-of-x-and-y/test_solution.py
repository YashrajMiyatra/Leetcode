import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [["X","Y","."],["Y",".","."]]
        self.assertEqual(self.solution.numberOfSubmatrices(grid), 3)

    def test_example_2(self):
        grid = [["X","X"],["X","Y"]]
        self.assertEqual(self.solution.numberOfSubmatrices(grid), 0)

    def test_example_3(self):
        grid = [[".","."],[".","."]]
        self.assertEqual(self.solution.numberOfSubmatrices(grid), 0)

if __name__ == '__main__':
    unittest.main()
