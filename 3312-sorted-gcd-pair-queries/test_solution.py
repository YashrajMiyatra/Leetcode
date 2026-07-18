import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.gcdValues([2,3,4], [0,2,2]), [1,2,2])

    def test_example_2(self):
        self.assertEqual(self.solution.gcdValues([4,4,2,1], [5,3,1,0]), [4,2,1,1])

    def test_example_3(self):
        self.assertEqual(self.solution.gcdValues([2,2], [0,0]), [2,2])

if __name__ == '__main__':
    unittest.main()
