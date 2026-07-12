import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minDays([1,10,3,10,2], 3, 1), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minDays([1,10,3,10,2], 3, 2), -1)

    def test_example_3(self):
        self.assertEqual(self.solution.minDays([7,7,7,7,12,7,7], 2, 3), 12)

if __name__ == '__main__':
    unittest.main()
