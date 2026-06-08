import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minBitwiseArray([2,3,5,7]), [-1,1,4,3])

    def test_example_2(self):
        self.assertEqual(self.solution.minBitwiseArray([11,13,31]), [9,12,15])

if __name__ == '__main__':
    unittest.main()
