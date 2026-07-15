import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        ans = self.solution.longestPalindrome("babad")
        self.assertTrue(ans in ["bab", "aba"])

    def test_example_2(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()
