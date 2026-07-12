import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.intToRoman(3749), "MMMDCCXLIX")

    def test_example_2(self):
        self.assertEqual(self.solution.intToRoman(58), "LVIII")

    def test_example_3(self):
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")

if __name__ == '__main__':
    unittest.main()
