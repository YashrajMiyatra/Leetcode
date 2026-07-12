import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.reversePairs([1,3,2,3,1]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.reversePairs([2,4,3,5,1]), 3)

if __name__ == '__main__':
    unittest.main()
