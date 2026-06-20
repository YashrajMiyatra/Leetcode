import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.repeatedStringMatch("abcd", "cdabcdab"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.repeatedStringMatch("a", "aa"), 2)

if __name__ == '__main__':
    unittest.main()
