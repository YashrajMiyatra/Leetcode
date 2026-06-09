import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumDifference([90], 1), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumDifference([9,4,1,7], 2), 2)

if __name__ == '__main__':
    unittest.main()
