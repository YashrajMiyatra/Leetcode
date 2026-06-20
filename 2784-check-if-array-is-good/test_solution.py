import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isGood([2, 1, 3]), False)

    def test_example_2(self):
        self.assertEqual(self.solution.isGood([1, 3, 3, 2]), True)

    def test_example_3(self):
        self.assertEqual(self.solution.isGood([1, 1]), True)

    def test_example_4(self):
        self.assertEqual(self.solution.isGood([3, 4, 4, 1, 2, 1]), False)

if __name__ == '__main__':
    unittest.main()
