import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countPrefixSuffixPairs(["a","aba","ababa","aa"]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.countPrefixSuffixPairs(["pa","papa","ma","mama"]), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.countPrefixSuffixPairs(["abab","ab"]), 0)

if __name__ == '__main__':
    unittest.main()
