import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.numberOfSpecialChars("aaAbcBC"), 3)

    def test_example2(self):
        self.assertEqual(self.sol.numberOfSpecialChars("abc"), 0)

    def test_example3(self):
        self.assertEqual(self.sol.numberOfSpecialChars("AbBCab"), 0)

    def test_lowercase_after_uppercase(self):
        # 'a' is lowercased after uppercased -> not special
        self.assertEqual(self.sol.numberOfSpecialChars("aAa"), 0)

    def test_no_lowercase(self):
        # 'A' has no lowercase -> not special
        self.assertEqual(self.sol.numberOfSpecialChars("A"), 0)

    def test_all_special(self):
        self.assertEqual(self.sol.numberOfSpecialChars("abAB"), 2)

    def test_multiple_occurrences(self):
        self.assertEqual(self.sol.numberOfSpecialChars("ababABAB"), 2)

if __name__ == '__main__':
    unittest.main()
