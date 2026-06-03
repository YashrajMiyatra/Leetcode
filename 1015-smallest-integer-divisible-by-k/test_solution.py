import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.smallestRepunitDivByK(1), 1)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.smallestRepunitDivByK(2), -1)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.smallestRepunitDivByK(3), 3)

    def test_coprime(self):
        s = Solution()
        self.assertEqual(s.smallestRepunitDivByK(7), 6)

    def test_multiple_of_5(self):
        s = Solution()
        self.assertEqual(s.smallestRepunitDivByK(15), -1)

if __name__ == '__main__':
    unittest.main()
