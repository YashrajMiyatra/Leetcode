import unittest
from solution import Solution

class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "abcabcbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    def test_example_2(self):
        s = "bbbbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

    def test_example_3(self):
        s = "pwwkew"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 0)

    def test_all_unique(self):
        s = "abcdef"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 6)

    def test_spaces_and_symbols(self):
        s = "a b!@#$ a"
        # " b!@#$ " has length 7
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 7)

    def test_duplicate_in_middle(self):
        s = "dvdf"
        # "vdf" has length 3
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

if __name__ == '__main__':
    unittest.main()
