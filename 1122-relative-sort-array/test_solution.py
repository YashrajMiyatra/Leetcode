import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]), [2,2,2,1,4,3,3,9,6,7,19])

    def test_example_2(self):
        self.assertEqual(self.solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]), [22,28,8,6,17,44])

if __name__ == '__main__':
    unittest.main()
