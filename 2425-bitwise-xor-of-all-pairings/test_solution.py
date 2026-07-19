import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.xorAllNums([2,1,3], [10,2,5,0]), 13)

    def test_example_2(self):
        self.assertEqual(self.solution.xorAllNums([1,2], [3,4]), 0)

if __name__ == '__main__':
    unittest.main()
