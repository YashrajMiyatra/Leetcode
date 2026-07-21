import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minMovesToSeat([3,1,5], [2,7,4]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.minMovesToSeat([4,1,5,9], [1,3,2,6]), 7)

    def test_example_3(self):
        self.assertEqual(self.solution.minMovesToSeat([2,2,6,6], [1,3,2,6]), 4)

if __name__ == '__main__':
    unittest.main()
