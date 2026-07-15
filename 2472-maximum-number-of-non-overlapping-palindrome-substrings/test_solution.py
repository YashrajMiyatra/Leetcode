import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxPalindromes("abaccdbbd", 3), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.maxPalindromes("adbcda", 2), 0)

if __name__ == '__main__':
    unittest.main()
