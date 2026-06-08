import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [9,12,5,10,14,3,10]
        pivot = 10
        self.assertEqual(self.solution.pivotArray(nums, pivot), [9,5,3,10,10,12,14])

    def test_example_2(self):
        nums = [-3,4,3,2]
        pivot = 2
        self.assertEqual(self.solution.pivotArray(nums, pivot), [-3,2,4,3])

if __name__ == '__main__':
    unittest.main()
