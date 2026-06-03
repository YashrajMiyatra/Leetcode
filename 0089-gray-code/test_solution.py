import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.grayCode(2), [0, 1, 3, 2])

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.grayCode(1), [0, 1])

    def test_zero(self):
        s = Solution()
        # Even though constraint is n >= 1, checking n=0
        self.assertEqual(s.grayCode(0), [0])

if __name__ == '__main__':
    unittest.main()
