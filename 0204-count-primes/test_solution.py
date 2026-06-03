import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.countPrimes(10), 4)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.countPrimes(0), 0)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.countPrimes(1), 0)

    def test_large(self):
        s = Solution()
        # Primes up to 5,000,000 is 348513
        self.assertEqual(s.countPrimes(5000000), 348513)

if __name__ == '__main__':
    unittest.main()
