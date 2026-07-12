import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.distance([1,3,1,1,2]), [5,0,3,4,0])

    def test_example_2(self):
        self.assertEqual(self.solution.distance([0,5,3]), [0,0,0])

if __name__ == '__main__':
    unittest.main()
