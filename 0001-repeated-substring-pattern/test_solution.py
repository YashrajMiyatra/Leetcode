import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.repeatedSubstringPattern("abab"), True)

    def test_example_2(self):
        self.assertEqual(self.solution.repeatedSubstringPattern("aba"), False)

    def test_example_3(self):
        self.assertEqual(self.solution.repeatedSubstringPattern("abcabcabcabc"), True)

if __name__ == '__main__':
    unittest.main()
