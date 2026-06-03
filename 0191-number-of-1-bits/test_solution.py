import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.hammingWeight(11), 3)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.hammingWeight(128), 1)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.hammingWeight(2147483645), 30)

if __name__ == '__main__':
    unittest.main()
