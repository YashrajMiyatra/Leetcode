import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        result = self.sol.longestPalindrome("babad")
        self.assertIn(result, ["bab", "aba"])

    def test_example2(self):
        self.assertEqual(self.sol.longestPalindrome("cbbd"), "bb")

    def test_single_char(self):
        self.assertEqual(self.sol.longestPalindrome("a"), "a")

    def test_all_same_chars(self):
        self.assertEqual(self.sol.longestPalindrome("aaaaa"), "aaaaa")

    def test_empty_string(self):
        self.assertEqual(self.sol.longestPalindrome(""), "")

    def test_entire_string_palindrome(self):
        self.assertEqual(self.sol.longestPalindrome("racecar"), "racecar")

if __name__ == '__main__':
    unittest.main()
