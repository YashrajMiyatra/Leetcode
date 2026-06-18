import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.angleClock(12, 30), 165.0, places=5)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.angleClock(3, 30), 75.0, places=5)

    def test_example_3(self):
        self.assertAlmostEqual(self.solution.angleClock(3, 15), 7.5, places=5)

if __name__ == '__main__':
    unittest.main()
