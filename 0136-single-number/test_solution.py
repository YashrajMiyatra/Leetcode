import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.singleNumber([2,2,1]), 1)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.singleNumber([4,1,2,1,2]), 4)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.singleNumber([1]), 1)

if __name__ == '__main__':
    unittest.main()
