import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findLength([1,2,3,2,1], [3,2,1,4,7]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.findLength([0,0,0,0,0], [0,0,0,0,0]), 5)

if __name__ == '__main__':
    unittest.main()
