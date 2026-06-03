import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(121))

    def test_example2(self):
        s = Solution()
        self.assertFalse(s.isPalindrome(-121))

    def test_example3(self):
        s = Solution()
        self.assertFalse(s.isPalindrome(10))

    def test_zero(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(0))

    def test_even_length(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(1221))

if __name__ == '__main__':
    unittest.main()
