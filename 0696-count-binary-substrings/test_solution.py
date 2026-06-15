import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countBinarySubstrings("00110011"), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.countBinarySubstrings("10101"), 4)

if __name__ == '__main__':
    unittest.main()
