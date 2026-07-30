import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.canIWin(10, 11))

    def test_example_2(self):
        self.assertTrue(self.solution.canIWin(10, 0))

    def test_example_3(self):
        self.assertTrue(self.solution.canIWin(10, 1))

if __name__ == '__main__':
    unittest.main()
