import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.constructTransformedArray([3,-2,1,1]), [1,1,1,3])

    def test_example_2(self):
        self.assertEqual(self.solution.constructTransformedArray([-1,4,-1]), [-1,-1,4])

if __name__ == '__main__':
    unittest.main()
