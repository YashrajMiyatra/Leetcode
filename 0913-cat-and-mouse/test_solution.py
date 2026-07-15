import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.catMouseGame([[1,3],[0],[3],[0,2]]), 1)

if __name__ == '__main__':
    unittest.main()
