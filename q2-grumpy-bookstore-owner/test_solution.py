import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3), 16)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSatisfied([1], [0], 1), 1)

if __name__ == '__main__':
    unittest.main()
