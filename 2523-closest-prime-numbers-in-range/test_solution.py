import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.closestPrimes(10, 19), [11, 13])

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.closestPrimes(4, 6), [-1, -1])

    def test_edge_case(self):
        s = Solution()
        self.assertEqual(s.closestPrimes(1, 1), [-1, -1])

    def test_two_and_three(self):
        s = Solution()
        # Gap of 1
        self.assertEqual(s.closestPrimes(1, 5), [2, 3])

if __name__ == '__main__':
    unittest.main()
