import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isStrictlyPalindromic(9), False)

    def test_example_2(self):
        self.assertEqual(self.solution.isStrictlyPalindromic(4), False)

if __name__ == '__main__':
    unittest.main()
