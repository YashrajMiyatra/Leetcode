import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_example_2(self):
        self.assertFalse(self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_example_3(self):
        self.assertTrue(self.solution.isInterleave("", "", ""))

if __name__ == '__main__':
    unittest.main()
