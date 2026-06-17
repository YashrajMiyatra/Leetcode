import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.concatenatedBinary(1), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.concatenatedBinary(3), 27)

    def test_example_3(self):
        self.assertEqual(self.solution.concatenatedBinary(12), 505379714)

if __name__ == '__main__':
    unittest.main()
