import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5), 6)

if __name__ == '__main__':
    unittest.main()
