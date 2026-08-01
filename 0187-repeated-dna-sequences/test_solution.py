import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC","CCCCCAAAAA"])

    def test_example_2(self):
        self.assertCountEqual(self.solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])

if __name__ == '__main__':
    unittest.main()
