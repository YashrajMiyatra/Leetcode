import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestPrefix("level"), "l")

    def test_example_2(self):
        self.assertEqual(self.solution.longestPrefix("ababab"), "abab")

    def test_edge_case(self):
        self.assertEqual(self.solution.longestPrefix("a"), "")
        self.assertEqual(self.solution.longestPrefix("aa"), "a")

if __name__ == '__main__':
    unittest.main()
