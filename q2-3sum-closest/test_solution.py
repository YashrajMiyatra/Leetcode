import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.threeSumClosest([-1,2,1,-4], 1), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.threeSumClosest([0,0,0], 1), 0)

if __name__ == '__main__':
    unittest.main()
