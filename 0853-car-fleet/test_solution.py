import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.carFleet(10, [3], [3]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.carFleet(100, [0,2,4], [4,2,1]), 1)

if __name__ == '__main__':
    unittest.main()
