import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.shortestPalindrome("aacecaaa"), "aaacecaaa")

    def test_example_2(self):
        self.assertEqual(self.solution.shortestPalindrome("abcd"), "dcbabcd")

    def test_edge_case(self):
        self.assertEqual(self.solution.shortestPalindrome(""), "")
        self.assertEqual(self.solution.shortestPalindrome("a"), "a")
        self.assertEqual(self.solution.shortestPalindrome("aa"), "aa")

if __name__ == '__main__':
    unittest.main()
