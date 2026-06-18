import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.nthPersonGetsNthSeat(1), 1.00000, places=5)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.nthPersonGetsNthSeat(2), 0.50000, places=5)

    def test_example_large(self):
        self.assertAlmostEqual(self.solution.nthPersonGetsNthSeat(100000), 0.50000, places=5)

if __name__ == '__main__':
    unittest.main()
