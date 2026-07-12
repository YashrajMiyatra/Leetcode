import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numOfStrings(["a","abc","bc","d"], "abc"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.numOfStrings(["a","b","c"], "aaaaabbbbb"), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.numOfStrings(["a","a","a"], "ab"), 3)

if __name__ == '__main__':
    unittest.main()
