import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximalPathQuality([0,32,10,43], [[0,1,10],[1,2,15],[0,3,10]], 49), 75)

    def test_example_2(self):
        self.assertEqual(self.solution.maximalPathQuality([5,10,15,20], [[0,1,10],[1,2,10],[0,3,10]], 30), 25)

if __name__ == '__main__':
    unittest.main()
