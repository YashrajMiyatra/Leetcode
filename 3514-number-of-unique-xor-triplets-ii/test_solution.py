import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.uniqueXORTriplets([1, 3]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.uniqueXORTriplets([6, 7, 8, 9]), 4)

if __name__ == '__main__':
    unittest.main()
