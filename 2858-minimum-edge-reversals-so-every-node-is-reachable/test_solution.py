import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minEdgeReversals(4, [[2,0],[2,1],[1,3]]), [1,1,0,2])

    def test_example_2(self):
        self.assertEqual(self.solution.minEdgeReversals(3, [[1,2],[2,0]]), [2,0,1])

if __name__ == '__main__':
    unittest.main()
