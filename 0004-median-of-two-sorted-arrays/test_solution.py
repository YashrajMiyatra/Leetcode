import unittest
from solution import Solution

class TestMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Example 1: nums1 = [1,3], nums2 = [2]
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.0)

    def test_example_2(self):
        # Example 2: nums1 = [1,2], nums2 = [3,4]
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.5)

    def test_one_empty_array_odd(self):
        nums1 = []
        nums2 = [1]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 1.0)

    def test_one_empty_array_even(self):
        nums1 = []
        nums2 = [1, 2, 3, 4]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.5)

    def test_single_element_each(self):
        nums1 = [1]
        nums2 = [2]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 1.5)

    def test_negative_numbers(self):
        nums1 = [-5, 3, 6, 12, 15]
        nums2 = [-12, -10, -6, -3, 4, 10]
        # Merged: [-12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15] (length 11, median is 3)
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 3.0)

    def test_identical_elements(self):
        nums1 = [1, 1]
        nums2 = [1, 1]
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 1.0)

    def test_disjoint_arrays(self):
        nums1 = [1, 2]
        nums2 = [10, 20, 30]
        # Merged: [1, 2, 10, 20, 30] -> median is 10.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 10.0)

if __name__ == '__main__':
    unittest.main()
