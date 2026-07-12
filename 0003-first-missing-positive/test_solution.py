import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.firstMissingPositive([1,2,0]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.firstMissingPositive([3,4,-1,1]), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.firstMissingPositive([7,8,9,11,12]), 1)

if __name__ == '__main__':
    unittest.main()
