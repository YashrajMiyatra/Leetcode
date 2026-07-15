import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countPalindromePaths([-1,0,0,1,1,2], "acaabc"), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.countPalindromePaths([-1,0,0,0,0], "aaaaa"), 10)

if __name__ == '__main__':
    unittest.main()
