import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
        self.assertEqual(self.solution.minCost(4, edges), 5)

    def test_example_2(self):
        edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
        self.assertEqual(self.solution.minCost(4, edges), 3)

if __name__ == '__main__':
    unittest.main()
