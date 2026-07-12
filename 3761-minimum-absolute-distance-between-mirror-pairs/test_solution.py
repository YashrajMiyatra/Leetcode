import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumDistance([12,21,45,33,54]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumDistance([120,21]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumDistance([21,120]), -1)

if __name__ == '__main__':
    unittest.main()
