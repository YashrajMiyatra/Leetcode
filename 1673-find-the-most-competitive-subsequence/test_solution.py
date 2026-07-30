import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.mostCompetitive([3,5,2,6], 2), [2,6])

    def test_example_2(self):
        self.assertEqual(self.solution.mostCompetitive([2,4,3,3,5,4,9,6], 4), [2,3,3,4])

if __name__ == '__main__':
    unittest.main()
