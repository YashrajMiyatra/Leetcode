import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1,2,3,0,0,0]
        self.solution.merge(nums1, 3, [2,5,6], 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_example_2(self):
        nums1 = [1]
        self.solution.merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        nums1 = [0]
        self.solution.merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

if __name__ == '__main__':
    unittest.main()
