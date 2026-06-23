import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.allPathsSourceTarget([[1,2],[3],[3],[]]), [[0,1,3],[0,2,3]])

    def test_example_2(self):
        self.assertEqual(self.solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]), [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])

if __name__ == '__main__':
    unittest.main()
