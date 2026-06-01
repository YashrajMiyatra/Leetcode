import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        self.assertEqual(s.sumFourDivisors([21,4,7]), 32)

    def test_example_2(self):
        s = Solution()
        self.assertEqual(s.sumFourDivisors([21,21]), 64)

    def test_example_3(self):
        s = Solution()
        self.assertEqual(s.sumFourDivisors([1,2,3,4,5]), 0)
        
    def test_eight(self):
        s = Solution()
        self.assertEqual(s.sumFourDivisors([8]), 15)  # 1 + 2 + 4 + 8 = 15

    def test_twelve(self):
        s = Solution()
        self.assertEqual(s.sumFourDivisors([12]), 0)  # 6 divisors

    def test_prime_cube(self):
        s = Solution()
        self.assertEqual(s.sumFourDivisors([27]), 40) # 1 + 3 + 9 + 27 = 40

if __name__ == '__main__':
    unittest.main()
