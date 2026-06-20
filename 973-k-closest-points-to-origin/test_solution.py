import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kClosest([[1,3],[-2,2]], 1), [[-2,2]])

    def test_example_2(self):
        # Result can be any order, so we sort the returned array to compare
        res = self.solution.kClosest([[3,3],[5,-1],[-2,4]], 2)
        res.sort()
        expected = [[-2,4], [3,3]]
        expected.sort()
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
