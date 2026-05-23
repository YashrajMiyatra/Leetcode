import unittest
from solution import Solution

class TestCheckSortedAndRotated(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertTrue(self.solution.check(nums))

    def test_example_2(self):
        nums = [2, 1, 3, 4]
        self.assertFalse(self.solution.check(nums))

    def test_example_3(self):
        nums = [1, 2, 3]
        self.assertTrue(self.solution.check(nums))

    def test_single_element(self):
        nums = [1]
        self.assertTrue(self.solution.check(nums))

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2]
        self.assertTrue(self.solution.check(nums))

    def test_duplicates_sorted_and_rotated(self):
        nums = [1, 2, 1]
        self.assertTrue(self.solution.check(nums))

    def test_duplicates_not_sorted_and_not_rotated(self):
        nums = [2, 1, 2, 1]
        self.assertFalse(self.solution.check(nums))

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        # [5, 4, 3, 2, 1] is sorted and rotated only if n <= 2.
        # For n = 5, it is not sorted and rotated.
        self.assertFalse(self.solution.check(nums))

if __name__ == '__main__':
    unittest.main()
