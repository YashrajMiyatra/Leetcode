import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        self.assertEqual(s.minimumCost([1,2,3]), 5)

    def test_example_2(self):
        s = Solution()
        self.assertEqual(s.minimumCost([6,5,7,9,2,2]), 23)
        
    def test_example_3(self):
        s = Solution()
        self.assertEqual(s.minimumCost([5,5]), 10)

    def test_single_candy(self):
        s = Solution()
        self.assertEqual(s.minimumCost([10]), 10)

if __name__ == '__main__':
    unittest.main()
