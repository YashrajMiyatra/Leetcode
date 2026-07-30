import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.nextGreaterElements([1,2,1]), [2,-1,2])

    def test_example_2(self):
        self.assertEqual(self.solution.nextGreaterElements([1,2,3,4,3]), [2,3,4,-1,4])

if __name__ == '__main__':
    unittest.main()
