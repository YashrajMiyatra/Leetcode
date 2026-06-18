import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minNumberOfSeconds(4, [2,1,1]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minNumberOfSeconds(10, [3,2,2,4]), 12)

    def test_example_3(self):
        self.assertEqual(self.solution.minNumberOfSeconds(5, [1]), 15)

if __name__ == '__main__':
    unittest.main()
