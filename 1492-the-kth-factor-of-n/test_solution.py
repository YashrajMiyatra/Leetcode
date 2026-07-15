import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kthFactor(12, 3), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.kthFactor(7, 2), 7)

    def test_example_3(self):
        self.assertEqual(self.solution.kthFactor(4, 4), -1)

if __name__ == '__main__':
    unittest.main()
