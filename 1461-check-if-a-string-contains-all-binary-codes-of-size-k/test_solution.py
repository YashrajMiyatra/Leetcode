import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.hasAllCodes("00110110", 2))

    def test_example_2(self):
        self.assertTrue(self.solution.hasAllCodes("0110", 1))

    def test_example_3(self):
        self.assertFalse(self.solution.hasAllCodes("0110", 2))

if __name__ == '__main__':
    unittest.main()
