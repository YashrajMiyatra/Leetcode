import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findKthLargest([3,2,1,5,6,4], 2), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)

if __name__ == '__main__':
    unittest.main()
