import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.trailingZeroes(3), 0)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.trailingZeroes(5), 1)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.trailingZeroes(0), 0)

    def test_large(self):
        s = Solution()
        self.assertEqual(s.trailingZeroes(100), 24)

if __name__ == '__main__':
    unittest.main()
