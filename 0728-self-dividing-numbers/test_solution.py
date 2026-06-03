import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(1, 22), [1,2,3,4,5,6,7,8,9,11,12,15,22])

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(47, 85), [48,55,66,77])

    def test_single_number_valid(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(128, 128), [128])

    def test_single_number_invalid_zero(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(10, 10), [])

if __name__ == '__main__':
    unittest.main()
