import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.trap([4,2,0,3,2,5]), 9)

if __name__ == '__main__':
    unittest.main()
