import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumWallsDestroyed([4], [3], [1,10]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumWallsDestroyed([10,2], [5,1], [5,2,7]), 3)

    def test_example_3(self):
        self.assertEqual(self.solution.maximumWallsDestroyed([1,2], [100,1], [10]), 0)

if __name__ == '__main__':
    unittest.main()
