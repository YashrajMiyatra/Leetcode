import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.getHappyString(1, 3), "c")

    def test_example_2(self):
        self.assertEqual(self.solution.getHappyString(1, 4), "")

    def test_example_3(self):
        self.assertEqual(self.solution.getHappyString(3, 9), "cab")

if __name__ == '__main__':
    unittest.main()
