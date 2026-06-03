import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertTrue(s.canMakeArithmeticProgression([3,5,1]))

    def test_example2(self):
        s = Solution()
        self.assertFalse(s.canMakeArithmeticProgression([1,2,4]))

    def test_two_elements(self):
        s = Solution()
        self.assertTrue(s.canMakeArithmeticProgression([1,100]))

    def test_zeros(self):
        s = Solution()
        self.assertTrue(s.canMakeArithmeticProgression([0,0,0,0]))

if __name__ == '__main__':
    unittest.main()
