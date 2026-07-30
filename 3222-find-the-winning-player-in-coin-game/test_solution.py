import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.winningPlayer(2, 7), "Alice")

    def test_example_2(self):
        self.assertEqual(self.solution.winningPlayer(4, 11), "Bob")

if __name__ == '__main__':
    unittest.main()
