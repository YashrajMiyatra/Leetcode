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
        self.assertEqual(self.sol.numberOfSpecialChars("abBCab"), 1)

    def test_single_special(self):
        self.assertEqual(self.sol.numberOfSpecialChars("zZ"), 1)

    def test_no_special(self):
        self.assertEqual(self.sol.numberOfSpecialChars("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)

    def test_all_special(self):
        self.assertEqual(self.sol.numberOfSpecialChars("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

if __name__ == '__main__':
    unittest.main()
