import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test_example_2(self):
        self.assertEqual(self.solution.longestCommonPrefix(["dog","racecar","car"]), "")

if __name__ == '__main__':
    unittest.main()
