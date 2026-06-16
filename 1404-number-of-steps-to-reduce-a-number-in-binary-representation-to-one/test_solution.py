import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numSteps("1101"), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.numSteps("10"), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.numSteps("1"), 0)

if __name__ == '__main__':
    unittest.main()
