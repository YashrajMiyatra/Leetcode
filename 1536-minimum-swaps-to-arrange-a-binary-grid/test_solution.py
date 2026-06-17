import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[0,0,1],[1,1,0],[1,0,0]]
        self.assertEqual(self.solution.minSwaps(grid), 3)

    def test_example_2(self):
        grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
        self.assertEqual(self.solution.minSwaps(grid), -1)

    def test_example_3(self):
        grid = [[1,0,0],[1,1,0],[1,1,1]]
        self.assertEqual(self.solution.minSwaps(grid), 0)

if __name__ == '__main__':
    unittest.main()
