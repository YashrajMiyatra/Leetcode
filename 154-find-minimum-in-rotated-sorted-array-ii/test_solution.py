import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMin([1,3,5]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.findMin([2,2,2,0,1]), 0)

if __name__ == '__main__':
    unittest.main()
