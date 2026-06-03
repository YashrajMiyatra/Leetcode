import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.maximizeSquareArea(4, 3, [2,3], [2]), 4)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maximizeSquareArea(6, 7, [2], [4]), -1)

    def test_large(self):
        s = Solution()
        self.assertEqual(s.maximizeSquareArea(10, 10, [2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9]), 81)

if __name__ == '__main__':
    unittest.main()
