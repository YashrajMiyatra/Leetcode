import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        self.assertEqual(s.maximumMEX([0,1,0]), [2,1])

    def test_example_2(self):
        s = Solution()
        self.assertEqual(s.maximumMEX([1,0,2]), [3])
        
    def test_example_3(self):
        s = Solution()
        self.assertEqual(s.maximumMEX([3,1]), [0,0])

    def test_tricky_zero_drop(self):
        s = Solution()
        self.assertEqual(s.maximumMEX([0,2,0,1]), [3])
        
    def test_identical(self):
        s = Solution()
        self.assertEqual(s.maximumMEX([0,1,1,0]), [2,2])

if __name__ == '__main__':
    unittest.main()
