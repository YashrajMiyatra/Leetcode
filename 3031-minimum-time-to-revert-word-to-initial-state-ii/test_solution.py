import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumTimeToInitialState("abacaba", 3), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumTimeToInitialState("abacaba", 4), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumTimeToInitialState("abcbabcd", 2), 4)

if __name__ == '__main__':
    unittest.main()
