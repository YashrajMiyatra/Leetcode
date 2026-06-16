import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kSmallestPairs([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]])

    def test_example_2(self):
        self.assertEqual(self.solution.kSmallestPairs([1,1,2], [1,2,3], 2), [[1,1],[1,1]])

if __name__ == '__main__':
    unittest.main()
