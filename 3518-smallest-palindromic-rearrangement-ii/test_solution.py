import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kthPalindromicPermutation("abba", 2), "baab")

    def test_example_2(self):
        self.assertEqual(self.solution.kthPalindromicPermutation("aa", 2), "")

    def test_example_3(self):
        self.assertEqual(self.solution.kthPalindromicPermutation("bacab", 1), "abcba")

if __name__ == '__main__':
    unittest.main()
