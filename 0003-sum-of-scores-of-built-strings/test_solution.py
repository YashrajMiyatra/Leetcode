import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.sumScores("babab"), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.sumScores("azbazbzaz"), 14)

    def test_edge_case(self):
        self.assertEqual(self.solution.sumScores("a"), 1)

if __name__ == '__main__':
    unittest.main()
