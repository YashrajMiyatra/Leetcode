import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countSubarrays([1,2,2,3], 2), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.countSubarrays([1,1,1,1], 1), 10)

    def test_example_3(self):
        self.assertEqual(self.solution.countSubarrays([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()
