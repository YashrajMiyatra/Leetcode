import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_example_2(self):
        self.assertEqual(self.solution.decodeString("3[a2[c]]"), "accaccacc")

    def test_example_3(self):
        self.assertEqual(self.solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

if __name__ == '__main__':
    unittest.main()
