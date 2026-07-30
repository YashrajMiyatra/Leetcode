import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxWidthRamp([6,0,8,2,1,5]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]), 7)

if __name__ == '__main__':
    unittest.main()
