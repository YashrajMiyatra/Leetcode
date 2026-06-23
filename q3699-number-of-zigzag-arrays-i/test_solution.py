import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numberOfZigZagArrays(3, 4, 5), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.numberOfZigZagArrays(3, 1, 3), 10)

if __name__ == '__main__':
    unittest.main()
