import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.sumGame("5023"))

    def test_example_2(self):
        self.assertTrue(self.solution.sumGame("25??"))

    def test_example_3(self):
        self.assertFalse(self.solution.sumGame("?3295???"))

if __name__ == '__main__':
    unittest.main()
