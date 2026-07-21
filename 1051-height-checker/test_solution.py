import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.heightChecker([1,1,4,2,1,3]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.heightChecker([5,1,2,3,4]), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.heightChecker([1,2,3,4,5]), 0)

if __name__ == '__main__':
    unittest.main()
