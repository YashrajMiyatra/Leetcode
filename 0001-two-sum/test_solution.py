import unittest
from solution import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        # 2 + 7 = 9, indices are [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        # 2 + 4 = 6, indices are [1, 2]
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        # 3 + 3 = 6, indices are [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        # -3 + 3 = 0, indices are [0, 2]
        self.assertEqual(self.solution.twoSum(nums, target), [0, 2])

    def test_large_numbers(self):
        nums = [10**9, 5, 2 * 10**9]
        target = 3 * 10**9
        # 10^9 + 2*10^9 = 3*10^9, indices are [0, 2]
        self.assertEqual(self.solution.twoSum(nums, target), [0, 2])

    def test_non_adjacent(self):
        nums = [1, 5, 10, 20, 3]
        target = 8
        # 5 + 3 = 8, indices are [1, 4]
        self.assertEqual(self.solution.twoSum(nums, target), [1, 4])

if __name__ == '__main__':
    unittest.main()
