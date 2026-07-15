import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isValid("()"))

    def test_example_2(self):
        self.assertTrue(self.solution.isValid("()[]{}"))

    def test_example_3(self):
        self.assertFalse(self.solution.isValid("(]"))

    def test_example_4(self):
        self.assertTrue(self.solution.isValid("([])"))

    def test_example_5(self):
        self.assertFalse(self.solution.isValid("([)]"))

if __name__ == '__main__':
    unittest.main()
