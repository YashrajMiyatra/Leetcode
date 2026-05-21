import unittest
from solution import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr1 = [1, 10, 100]
        arr2 = [1000]
        self.assertEqual(self.solution.longestCommonPrefix(arr1, arr2), 3)

    def test_example_2(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 4, 4]
        self.assertEqual(self.solution.longestCommonPrefix(arr1, arr2), 0)

    def test_single_element_exact_match(self):
        arr1 = [12345]
        arr2 = [12345]
        self.assertEqual(self.solution.longestCommonPrefix(arr1, arr2), 5)

    def test_single_element_partial_match(self):
        arr1 = [1234567]
        arr2 = [123489]
        self.assertEqual(self.solution.longestCommonPrefix(arr1, arr2), 4)

    def test_large_numbers_no_common(self):
        arr1 = [98765432]
        arr2 = [12345678]
        self.assertEqual(self.solution.longestCommonPrefix(arr1, arr2), 0)

    def test_multiple_potential_matches(self):
        arr1 = [123, 456, 789]
        arr2 = [1234, 45, 78]
        # Common prefix pairs:
        # (123, 1234) -> prefix 123, len 3
        # (456, 45) -> prefix 45, len 2
        # (789, 78) -> prefix 78, len 2
        # Longest is 3.
        self.assertEqual(self.solution.longestCommonPrefix(arr1, arr2), 3)

if __name__ == '__main__':
    unittest.main()
