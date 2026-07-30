import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.find132pattern([1, 2, 3, 4]))

    def test_example_2(self):
        self.assertTrue(self.solution.find132pattern([3, 1, 4, 2]))

    def test_example_3(self):
        self.assertTrue(self.solution.find132pattern([-1, 3, 2, 0]))

if __name__ == '__main__':
    unittest.main()
