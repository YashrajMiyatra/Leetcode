import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.mirrorReflection(2, 1), 2)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.mirrorReflection(3, 1), 1)

    def test_even_even(self):
        s = Solution()
        # 6 and 4 -> 3 and 2 -> p odd, q even -> 0
        self.assertEqual(s.mirrorReflection(6, 4), 0)

    def test_odd_odd(self):
        s = Solution()
        # 15 and 5 -> both odd -> 1
        self.assertEqual(s.mirrorReflection(15, 5), 1)

if __name__ == '__main__':
    unittest.main()
