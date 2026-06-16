import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.timeRequiredToBuy([2,3,2], 2), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.timeRequiredToBuy([5,1,1,1], 0), 8)

if __name__ == '__main__':
    unittest.main()
