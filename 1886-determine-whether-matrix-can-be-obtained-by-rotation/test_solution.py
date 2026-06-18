import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        mat = [[0,1],[1,0]]
        target = [[1,0],[0,1]]
        self.assertTrue(self.solution.findRotation(mat, target))

    def test_example_2(self):
        mat = [[0,1],[1,1]]
        target = [[1,0],[0,1]]
        self.assertFalse(self.solution.findRotation(mat, target))

    def test_example_3(self):
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        target = [[1,1,1],[0,1,0],[0,0,0]]
        self.assertTrue(self.solution.findRotation(mat, target))

if __name__ == '__main__':
    unittest.main()
