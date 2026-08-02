import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.solution.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    def test_example_2(self):
        self.assertCountEqual(self.solution.letterCombinations("2"), ["a","b","c"])

if __name__ == '__main__':
    unittest.main()
