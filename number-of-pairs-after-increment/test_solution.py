import unittest
from solution import Solution

class TestNumberOfPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        queries = [[2, 5], [1, 0, 0, 2], [2, 5]]
        expected = [2, 1]
        self.assertEqual(self.solution.numberOfPairs(nums1, nums2, queries), expected)

    def test_example_2(self):
        nums1 = [1, 1]
        nums2 = [2, 2, 3]
        queries = [[2, 4], [1, 0, 1, 1], [2, 4]]
        expected = [2, 6]
        self.assertEqual(self.solution.numberOfPairs(nums1, nums2, queries), expected)

    def test_example_3(self):
        nums1 = [2, 5, 8, 4]
        nums2 = [1, 3, 8]
        queries = [[2, 9], [1, 1, 2, 1], [2, 10]]
        expected = [1, 0]
        self.assertEqual(self.solution.numberOfPairs(nums1, nums2, queries), expected)

    def test_single_elements(self):
        nums1 = [5]
        nums2 = [10]
        queries = [[2, 15], [1, 0, 0, 5], [2, 15], [2, 20]]
        expected = [1, 0, 1]
        self.assertEqual(self.solution.numberOfPairs(nums1, nums2, queries), expected)

    def test_large_value_adds(self):
        nums1 = [1]
        nums2 = [2] * 10
        queries = [[2, 3], [1, 0, 9, 100000], [2, 100003]]
        expected = [10, 10]
        self.assertEqual(self.solution.numberOfPairs(nums1, nums2, queries), expected)

if __name__ == '__main__':
    unittest.main()
