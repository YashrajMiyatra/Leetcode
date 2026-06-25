import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumWeight(6, [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], 0, 1, 5), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumWeight(3, [[0,1,1],[2,1,1]], 0, 1, 2), -1)

if __name__ == '__main__':
    unittest.main()
