import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.minScore(4, [[1,2,2],[1,3,4],[3,4,7]]), 2)

if __name__ == '__main__':
    unittest.main()
