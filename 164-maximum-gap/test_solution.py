import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumGap([3,6,9,1]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumGap([10]), 0)

if __name__ == '__main__':
    unittest.main()
