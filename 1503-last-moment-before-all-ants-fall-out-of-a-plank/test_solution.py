import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.getLastMoment(4, [4,3], [0,1]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.getLastMoment(7, [], [0,1,2,3,4,5,6,7]), 7)

    def test_example_3(self):
        self.assertEqual(self.solution.getLastMoment(7, [0,1,2,3,4,5,6,7], []), 7)

if __name__ == '__main__':
    unittest.main()
