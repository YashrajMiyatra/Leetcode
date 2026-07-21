import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestCommonSubpath(5, [[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.longestCommonSubpath(3, [[0],[1],[2]]), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.longestCommonSubpath(5, [[0,1,2,3,4],[4,3,2,1,0]]), 1)

if __name__ == '__main__':
    unittest.main()
