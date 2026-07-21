import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.smallestPalindromicRearrangement("z"), "z")

    def test_example_2(self):
        self.assertEqual(self.solution.smallestPalindromicRearrangement("babab"), "abbba")

    def test_example_3(self):
        self.assertEqual(self.solution.smallestPalindromicRearrangement("daccad"), "acddca")

if __name__ == '__main__':
    unittest.main()
