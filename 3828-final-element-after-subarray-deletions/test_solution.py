import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximizeFinalElement([1,5,2]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.maximizeFinalElement([3,7]), 7)

if __name__ == '__main__':
    unittest.main()
