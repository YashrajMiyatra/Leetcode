import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestWord(["w","wo","wor","worl","world"]), "world")

    def test_example_2(self):
        self.assertEqual(self.solution.longestWord(["a","banana","app","appl","ap","apply","apple"]), "apple")

if __name__ == '__main__':
    unittest.main()
