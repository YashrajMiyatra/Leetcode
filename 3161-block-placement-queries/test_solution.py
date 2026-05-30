import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]
        expected = [False, True, True]
        self.assertEqual(self.sol.getResults(queries), expected)

    def test_example2(self):
        queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]
        expected = [True, True, False]
        self.assertEqual(self.sol.getResults(queries), expected)

    def test_no_obstacles(self):
        queries = [[2, 5, 5], [2, 5, 6]]
        expected = [True, False]
        self.assertEqual(self.sol.getResults(queries), expected)

    def test_exact_fit_between_obstacles(self):
        queries = [[1, 2], [1, 5], [2, 5, 3], [2, 5, 4]]
        # Gaps: [0, 2] size 2, [2, 5] size 3.
        # Queries: size 3 in [0, 5] -> True (fits between 2 and 5). Size 4 -> False.
        expected = [True, False]
        self.assertEqual(self.sol.getResults(queries), expected)

    def test_multiple_merges(self):
        queries = [[1, 1], [1, 10], [1, 4], [2, 10, 6], [2, 10, 7]]
        # Obstacles: 1, 4, 10
        # Gaps: [0, 1] size 1, [1, 4] size 3, [4, 10] size 6
        expected = [True, False]
        self.assertEqual(self.sol.getResults(queries), expected)

if __name__ == '__main__':
    unittest.main()
