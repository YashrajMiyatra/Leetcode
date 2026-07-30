import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumPushes("abcde"), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumPushes("xycdefghij"), 12)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumPushes("abcdefghijklmnopqrstuvwxyz"), 54)

if __name__ == '__main__':
    unittest.main()
