import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        self.assertEqual(self.solution.flipSquareSubmatrix(grid, 1, 0, 3), [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]])

    def test_example_2(self):
        grid = [[3,4,2,3],[2,3,4,2]]
        self.assertEqual(self.solution.flipSquareSubmatrix(grid, 0, 2, 2), [[3,4,4,2],[2,3,2,3]])

if __name__ == '__main__':
    unittest.main()
