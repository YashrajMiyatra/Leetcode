import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.gcdOfSums(4), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.gcdOfSums(5), 5)

if __name__ == '__main__':
    unittest.main()
