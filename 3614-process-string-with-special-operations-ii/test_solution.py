import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.processString("a#b%*", 1), "a")

    def test_example_2(self):
        self.assertEqual(self.solution.processString("cd%#*#", 3), "d")

    def test_example_3(self):
        self.assertEqual(self.solution.processString("z*#", 0), ".")

if __name__ == '__main__':
    unittest.main()
