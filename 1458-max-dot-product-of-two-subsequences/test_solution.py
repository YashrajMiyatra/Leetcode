import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.maxDotProduct([2,1,-2,5], [3,0,-6]), 18)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maxDotProduct([3,-2], [2,-6,7]), 21)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.maxDotProduct([-1,-1], [1,1]), -1)

    def test_negative_reverse(self):
        s = Solution()
        self.assertEqual(s.maxDotProduct([1,1], [-1,-1]), -1)

    def test_with_zero(self):
        s = Solution()
        self.assertEqual(s.maxDotProduct([-1,-1], [0,1]), 0)

if __name__ == '__main__':
    unittest.main()
