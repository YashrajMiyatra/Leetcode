import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12), -1)

if __name__ == '__main__':
    unittest.main()
