import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.maxMatrixSum([[1,-1],[-1,1]]), 4)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]), 16)

    def test_with_zero(self):
        s = Solution()
        self.assertEqual(s.maxMatrixSum([[0,-1],[1,2]]), 4)

    def test_all_negative(self):
        s = Solution()
        self.assertEqual(s.maxMatrixSum([[-1,-2],[-3,-4]]), 10)

if __name__ == '__main__':
    unittest.main()
