import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6])

    def test_example_2(self):
        self.assertEqual(self.solution.findDisappearedNumbers([1,1]), [2])

if __name__ == '__main__':
    unittest.main()
