import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.waysToMakeFair([2,1,6,4]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.waysToMakeFair([1,1,1]), 3)

    def test_example_3(self):
        self.assertEqual(self.solution.waysToMakeFair([1,2,3]), 0)

if __name__ == '__main__':
    unittest.main()
