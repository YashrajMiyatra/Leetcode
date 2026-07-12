import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMin([3,4,5,1,2]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.findMin([4,5,6,7,0,1,2]), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.findMin([11,13,15,17]), 11)

if __name__ == '__main__':
    unittest.main()
