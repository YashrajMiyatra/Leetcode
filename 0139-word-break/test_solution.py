import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.wordBreak("leetcode", ["leet","code"]))

    def test_example_2(self):
        self.assertTrue(self.solution.wordBreak("applepenapple", ["apple","pen"]))

    def test_example_3(self):
        self.assertFalse(self.solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

if __name__ == '__main__':
    unittest.main()
