import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxProduct("ababbb"), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProduct("zaaaxbbby"), 9)

if __name__ == '__main__':
    unittest.main()
