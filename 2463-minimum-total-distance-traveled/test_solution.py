import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumTotalDistance([0,4,6], [[2,2],[6,2]]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumTotalDistance([1,-1], [[-2,1],[2,1]]), 2)

if __name__ == '__main__':
    unittest.main()
