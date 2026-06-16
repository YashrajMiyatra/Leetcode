import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isPossible([9,3,5]), True)

    def test_example_2(self):
        self.assertEqual(self.solution.isPossible([1,1,1,2]), False)

    def test_example_3(self):
        self.assertEqual(self.solution.isPossible([8,5]), True)

if __name__ == '__main__':
    unittest.main()
