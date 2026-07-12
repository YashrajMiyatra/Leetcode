import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rotateGrid([[40,10],[30,20]], 1), [[10,20],[40,30]])

    def test_example_2(self):
        self.assertEqual(self.solution.rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2), [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]])

if __name__ == '__main__':
    unittest.main()
