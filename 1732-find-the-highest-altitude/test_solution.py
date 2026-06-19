import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.largestAltitude([-5,1,5,0,-7]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.largestAltitude([-4,-3,-2,-1,4,3,2]), 0)

if __name__ == '__main__':
    unittest.main()
