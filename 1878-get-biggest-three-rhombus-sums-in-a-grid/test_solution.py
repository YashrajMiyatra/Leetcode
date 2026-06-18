import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
        self.assertEqual(self.solution.getBiggestThree(grid), [228, 216, 211])

    def test_example_2(self):
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(self.solution.getBiggestThree(grid), [20, 9, 8])

    def test_example_3(self):
        grid = [[7,7,7]]
        self.assertEqual(self.solution.getBiggestThree(grid), [7])

if __name__ == '__main__':
    unittest.main()
