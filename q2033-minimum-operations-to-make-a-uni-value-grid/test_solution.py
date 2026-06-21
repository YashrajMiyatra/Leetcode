import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minOperations([[2,4],[6,8]], 2), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.minOperations([[1,5],[2,3]], 1), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.minOperations([[1,2],[3,4]], 2), -1)

if __name__ == '__main__':
    unittest.main()
