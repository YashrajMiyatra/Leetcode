import unittest
from solution import Solution

class TestSearchRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_example_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example_3(self):
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_target_at_left_boundary(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_target_at_right_boundary(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        self.assertEqual(self.solution.search(nums, target), 6)

    def test_small_rotation(self):
        nums = [2, 3, 4, 5, 1]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_no_rotation(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)

if __name__ == '__main__':
    unittest.main()
