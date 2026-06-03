import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.getPermutation(3, 3), "213")

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.getPermutation(4, 9), "2314")

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.getPermutation(3, 1), "123")

    def test_max_constraints(self):
        s = Solution()
        # 9! = 362880
        self.assertEqual(s.getPermutation(9, 362880), "987654321")

if __name__ == '__main__':
    unittest.main()
