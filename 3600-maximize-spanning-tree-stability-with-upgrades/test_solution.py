import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        edges = [[0,1,2,1],[1,2,3,0]]
        self.assertEqual(self.solution.maximizeStability(3, edges, 1), 2)

    def test_example_2(self):
        edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
        self.assertEqual(self.solution.maximizeStability(3, edges, 2), 6)

    def test_example_3(self):
        edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
        self.assertEqual(self.solution.maximizeStability(3, edges, 0), -1)

if __name__ == '__main__':
    unittest.main()
