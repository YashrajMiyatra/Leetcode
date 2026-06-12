import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.assignEdgeWeights([[1,2]], [[1,1],[1,2]]), [0,1])

    def test_example_2(self):
        self.assertEqual(self.solution.assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]], [[1,4],[3,4],[2,5]]), [2,1,4])

if __name__ == '__main__':
    unittest.main()
