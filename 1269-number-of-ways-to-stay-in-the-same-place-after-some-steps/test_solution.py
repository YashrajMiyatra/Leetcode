import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numWays(3, 2), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.numWays(2, 4), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.numWays(4, 2), 8)

if __name__ == '__main__':
    unittest.main()
