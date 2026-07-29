import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.uniqueXORTriplets([1, 2]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.uniqueXORTriplets([3, 1, 2]), 4)
        
    def test_n_4(self):
        self.assertEqual(self.solution.uniqueXORTriplets([1, 2, 3, 4]), 8)

if __name__ == '__main__':
    unittest.main()
