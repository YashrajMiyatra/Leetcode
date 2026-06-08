import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
        threshold = 4
        self.assertEqual(self.solution.maxSideLength(mat, threshold), 2)

    def test_example_2(self):
        mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
        threshold = 1
        self.assertEqual(self.solution.maxSideLength(mat, threshold), 0)

if __name__ == '__main__':
    unittest.main()
