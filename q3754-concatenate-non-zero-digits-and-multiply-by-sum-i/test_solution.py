import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.concatenateAndMultiply(10203004), 12340)

    def test_example_2(self):
        self.assertEqual(self.solution.concatenateAndMultiply(1000), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.concatenateAndMultiply(0), 0)

if __name__ == '__main__':
    unittest.main()
