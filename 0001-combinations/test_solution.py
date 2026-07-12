import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.combine(4, 2)
        expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        self.assertEqual(self.solution.combine(1, 1), [[1]])

if __name__ == '__main__':
    unittest.main()
