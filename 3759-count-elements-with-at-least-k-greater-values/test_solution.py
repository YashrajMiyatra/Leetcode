import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countElements([3,1,2], 1), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.countElements([5,5,5], 2), 0)

if __name__ == '__main__':
    unittest.main()
