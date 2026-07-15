import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]), 20)

    def test_example_2(self):
        self.assertEqual(self.solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]), 18)

if __name__ == '__main__':
    unittest.main()
