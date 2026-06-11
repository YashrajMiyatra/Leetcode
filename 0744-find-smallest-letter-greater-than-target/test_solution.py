import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.nextGreatestLetter(["c","f","j"], "a"), "c")

    def test_example_2(self):
        self.assertEqual(self.solution.nextGreatestLetter(["c","f","j"], "c"), "f")

    def test_example_3(self):
        self.assertEqual(self.solution.nextGreatestLetter(["x","x","y","y"], "z"), "x")

if __name__ == '__main__':
    unittest.main()
