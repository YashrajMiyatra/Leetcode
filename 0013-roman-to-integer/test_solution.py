import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_example_3(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

if __name__ == '__main__':
    unittest.main()
