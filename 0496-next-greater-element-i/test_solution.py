import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.nextGreaterElement([4,1,2], [1,3,4,2]), [-1,3,-1])

    def test_example_2(self):
        self.assertEqual(self.solution.nextGreaterElement([2,4], [1,2,3,4]), [3,-1])

if __name__ == '__main__':
    unittest.main()
