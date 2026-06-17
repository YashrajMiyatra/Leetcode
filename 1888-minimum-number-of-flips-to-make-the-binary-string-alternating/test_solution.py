import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minFlips("111000"), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.minFlips("010"), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.minFlips("1110"), 1)

if __name__ == '__main__':
    unittest.main()
