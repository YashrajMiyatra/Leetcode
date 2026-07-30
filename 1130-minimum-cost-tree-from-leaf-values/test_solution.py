import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.mctFromLeafValues([6,2,4]), 32)

    def test_example_2(self):
        self.assertEqual(self.solution.mctFromLeafValues([4,11]), 44)

if __name__ == '__main__':
    unittest.main()
