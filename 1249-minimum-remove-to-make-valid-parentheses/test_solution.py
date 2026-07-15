import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        ans = self.solution.minRemoveToMakeValid("lee(t(c)o)de)")
        self.assertTrue(ans in ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"])

    def test_example_2(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("a)b(c)d"), "ab(c)d")

    def test_example_3(self):
        self.assertEqual(self.solution.minRemoveToMakeValid("))(("), "")

if __name__ == '__main__':
    unittest.main()
