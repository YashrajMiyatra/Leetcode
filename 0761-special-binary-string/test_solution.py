import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.makeLargestSpecial("11011000"), "11100100")

    def test_example_2(self):
        self.assertEqual(self.solution.makeLargestSpecial("10"), "10")

if __name__ == '__main__':
    unittest.main()
