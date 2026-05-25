import unittest
from solution import Solution

class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 2, 1]
        self.assertEqual(self.solution.minOperations(nums), 2)

    def test_example_2(self):
        nums = [1, 0, 2]
        self.assertEqual(self.solution.minOperations(nums), 2)

    def test_example_3(self):
        nums = [2, 0, 1, 3]
        self.assertEqual(self.solution.minOperations(nums), -1)

    def test_single_element(self):
        nums = [0]
        self.assertEqual(self.solution.minOperations(nums), 0)

    def test_already_sorted(self):
        nums = [0, 1, 2, 3, 4]
        self.assertEqual(self.solution.minOperations(nums), 0)

    def test_only_reverse(self):
        # Reverse [4, 3, 2, 1, 0] to [0, 1, 2, 3, 4] in 1 operation (R).
        nums = [4, 3, 2, 1, 0]
        self.assertEqual(self.solution.minOperations(nums), 1)

    def test_only_rotations(self):
        # [2, 3, 4, 0, 1] requires 3 left rotations to sort.
        nums = [2, 3, 4, 0, 1]
        self.assertEqual(self.solution.minOperations(nums), 3)

    def test_impossible_permutation(self):
        # Even if valid permutation, relative order is scrambled.
        nums = [1, 3, 0, 2]
        self.assertEqual(self.solution.minOperations(nums), -1)

if __name__ == '__main__':
    unittest.main()
