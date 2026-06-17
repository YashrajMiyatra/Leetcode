import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        mat = [[1,0,0],[0,0,1],[1,0,0]]
        self.assertEqual(self.solution.numSpecial(mat), 1)

    def test_example_2(self):
        mat = [[1,0,0],[0,1,0],[0,0,1]]
        self.assertEqual(self.solution.numSpecial(mat), 3)

if __name__ == '__main__':
    unittest.main()
