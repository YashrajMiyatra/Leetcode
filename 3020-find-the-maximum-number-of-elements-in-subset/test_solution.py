import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumLength([5,4,1,2,2]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumLength([1,3,2,4]), 1)

    def test_ones(self):
        self.assertEqual(self.solution.maximumLength([1,1,1,1]), 3)
        self.assertEqual(self.solution.maximumLength([1,1,1,1,1]), 5)
        self.assertEqual(self.solution.maximumLength([1]), 1)
        self.assertEqual(self.solution.maximumLength([1,1]), 1)

if __name__ == '__main__':
    unittest.main()
