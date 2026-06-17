import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minOperations("0100"), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minOperations("10"), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.minOperations("1111"), 2)

if __name__ == '__main__':
    unittest.main()
