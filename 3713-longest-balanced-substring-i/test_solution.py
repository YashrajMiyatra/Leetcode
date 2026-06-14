import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestBalancedSubstring("abbac"), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.longestBalancedSubstring("zzabccy"), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.longestBalancedSubstring("aba"), 2)

if __name__ == '__main__':
    unittest.main()
