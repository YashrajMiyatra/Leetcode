import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countPrimeSetBits(6, 10), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.countPrimeSetBits(10, 15), 5)

if __name__ == '__main__':
    unittest.main()
