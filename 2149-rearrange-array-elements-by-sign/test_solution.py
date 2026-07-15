import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rearrangeArray([3,1,-2,-5,2,-4]), [3,-2,1,-5,2,-4])

    def test_example_2(self):
        self.assertEqual(self.solution.rearrangeArray([-1,1]), [1,-1])

if __name__ == '__main__':
    unittest.main()
