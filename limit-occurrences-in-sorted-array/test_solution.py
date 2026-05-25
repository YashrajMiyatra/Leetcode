import unittest
from solution import Solution

class TestLimitOccurrences(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 1, 2, 2, 3]
        # In-place check
        res = self.solution.limitOccurrences(nums, k)
        self.assertEqual(res, expected)
        self.assertEqual(nums[:len(expected)], expected)

    def test_example_2(self):
        nums = [1, 2, 3]
        k = 1
        expected = [1, 2, 3]
        res = self.solution.limitOccurrences(nums, k)
        self.assertEqual(res, expected)
        self.assertEqual(nums[:len(expected)], expected)

    def test_empty_array(self):
        nums = []
        k = 2
        expected = []
        res = self.solution.limitOccurrences(nums, k)
        self.assertEqual(res, expected)

    def test_single_element(self):
        nums = [5]
        k = 1
        expected = [5]
        res = self.solution.limitOccurrences(nums, k)
        self.assertEqual(res, expected)

    def test_k_greater_than_length(self):
        nums = [1, 1, 2, 2, 3]
        k = 10
        expected = [1, 1, 2, 2, 3]
        res = self.solution.limitOccurrences(nums, k)
        self.assertEqual(res, expected)

    def test_large_k_duplicates(self):
        nums = [1, 1, 1, 1, 1]
        k = 3
        expected = [1, 1, 1]
        res = self.solution.limitOccurrences(nums, k)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
