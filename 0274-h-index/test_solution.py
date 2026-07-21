import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.hIndex([3,0,6,1,5]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.hIndex([1,3,1]), 1)

if __name__ == '__main__':
    unittest.main()
