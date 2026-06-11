import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumCost([1,2,3,12]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumCost([5,4,3]), 12)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumCost([10,3,1,1]), 12)

if __name__ == '__main__':
    unittest.main()
