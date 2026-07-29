import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maxTaskAssign([5, 4], [0, 0, 0], 1, 5), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maxTaskAssign([10, 15, 30], [0, 10, 10, 10, 10], 3, 10), 2)

if __name__ == '__main__':
    unittest.main()
