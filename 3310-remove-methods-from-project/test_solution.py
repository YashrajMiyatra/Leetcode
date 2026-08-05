import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.solution.remainingMethods(4, 1, [[1,2],[0,1],[3,2]]), [0,1,2,3])

    def test_example_2(self):
        self.assertCountEqual(self.solution.remainingMethods(5, 0, [[1,2],[0,2],[0,1],[3,4]]), [3,4])

    def test_example_3(self):
        self.assertCountEqual(self.solution.remainingMethods(3, 2, [[1,2],[0,1],[2,0]]), [])

if __name__ == '__main__':
    unittest.main()
