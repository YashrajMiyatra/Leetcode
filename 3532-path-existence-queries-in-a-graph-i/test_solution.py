import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.pathExists(2, [1,3], 1, [[0,0],[0,1]]), [True, False])

    def test_example_2(self):
        self.assertEqual(self.solution.pathExists(4, [2,5,6,8], 2, [[0,1],[0,2],[1,3],[2,3]]), [False, False, True, True])

if __name__ == '__main__':
    unittest.main()
