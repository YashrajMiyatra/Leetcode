import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.magicalString(6), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.magicalString(1), 1)

    def test_edge_case(self):
        self.assertEqual(self.solution.magicalString(0), 0)
        self.assertEqual(self.solution.magicalString(3), 1)

if __name__ == '__main__':
    unittest.main()
