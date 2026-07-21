import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minImpossibleOR([2,1]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.minImpossibleOR([5,3,2]), 1)

if __name__ == '__main__':
    unittest.main()
