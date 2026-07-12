import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumPathScore([[0, 1],[2, 0]], 1), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumPathScore([[0, 1],[1, 2]], 1), -1)

if __name__ == '__main__':
    unittest.main()
