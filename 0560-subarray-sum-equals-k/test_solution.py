import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.subarraySum([1,1,1], 2), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.subarraySum([1,2,3], 3), 2)

if __name__ == '__main__':
    unittest.main()
