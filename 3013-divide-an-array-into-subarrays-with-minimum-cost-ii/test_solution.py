import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumCost([1,3,2,6,4,2], 3, 3), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumCost([10,1,2,2,2,1], 4, 3), 15)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumCost([10,8,18,9], 3, 1), 36)

if __name__ == '__main__':
    unittest.main()
