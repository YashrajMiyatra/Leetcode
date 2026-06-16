import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.validMountainArray([2,1]), False)

    def test_example_2(self):
        self.assertEqual(self.solution.validMountainArray([3,5,5]), False)

    def test_example_3(self):
        self.assertEqual(self.solution.validMountainArray([0,3,2,1]), True)

if __name__ == '__main__':
    unittest.main()
