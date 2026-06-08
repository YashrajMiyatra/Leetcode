import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        self.assertEqual(self.solution.maximalRectangle(matrix), 6)

    def test_example_2(self):
        matrix = [["0"]]
        self.assertEqual(self.solution.maximalRectangle(matrix), 0)

    def test_example_3(self):
        matrix = [["1"]]
        self.assertEqual(self.solution.maximalRectangle(matrix), 1)

if __name__ == '__main__':
    unittest.main()
