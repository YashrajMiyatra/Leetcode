import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.findArray([5,2,0,3,1]), [5,7,2,3,2])

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.findArray([13]), [13])

    def test_zero(self):
        s = Solution()
        self.assertEqual(s.findArray([0,0,0]), [0,0,0])

if __name__ == '__main__':
    unittest.main()
