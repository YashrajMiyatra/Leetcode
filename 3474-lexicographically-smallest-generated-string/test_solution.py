import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.generateString("TFTF", "ab"), "ababa")

    def test_example_2(self):
        self.assertEqual(self.solution.generateString("TFTF", "abc"), "")

    def test_example_3(self):
        self.assertEqual(self.solution.generateString("F", "d"), "a")

if __name__ == '__main__':
    unittest.main()
