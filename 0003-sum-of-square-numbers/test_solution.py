import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.judgeSquareSum(5), True)

    def test_example_2(self):
        self.assertEqual(self.solution.judgeSquareSum(3), False)

if __name__ == '__main__':
    unittest.main()
