import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lastStoneWeight([2,7,4,1,8,1]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.lastStoneWeight([1]), 1)

if __name__ == '__main__':
    unittest.main()
