import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findGCD([2,5,6,9,10]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.findGCD([7,5,6,8,3]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.findGCD([3,3]), 3)

if __name__ == '__main__':
    unittest.main()
