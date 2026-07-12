import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.getCommon([1,2,3], [2,4]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.getCommon([1,2,3,6], [2,3,4,5]), 2)

if __name__ == '__main__':
    unittest.main()
