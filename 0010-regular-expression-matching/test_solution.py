import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isMatch("aa", "a"), False)

    def test_example_2(self):
        self.assertEqual(self.solution.isMatch("aa", "a*"), True)

    def test_example_3(self):
        self.assertEqual(self.solution.isMatch("ab", ".*"), True)

if __name__ == '__main__':
    unittest.main()
