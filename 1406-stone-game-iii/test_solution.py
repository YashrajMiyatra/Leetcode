import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, 7]), "Bob")

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, -9]), "Alice")

    def test_example_3(self):
        self.assertEqual(self.solution.stoneGameIII([1, 2, 3, 6]), "Tie")

if __name__ == '__main__':
    unittest.main()
