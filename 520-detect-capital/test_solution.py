import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.detectCapitalUse("USA"))

    def test_example_2(self):
        self.assertFalse(self.solution.detectCapitalUse("FlaG"))

    def test_all_lower(self):
        self.assertTrue(self.solution.detectCapitalUse("leetcode"))

    def test_title(self):
        self.assertTrue(self.solution.detectCapitalUse("Google"))

    def test_single_upper(self):
        self.assertTrue(self.solution.detectCapitalUse("A"))

    def test_single_lower(self):
        self.assertTrue(self.solution.detectCapitalUse("a"))

if __name__ == '__main__':
    unittest.main()
