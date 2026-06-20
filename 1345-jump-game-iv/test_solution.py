import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minJumps([100,-23,-23,404,100,23,23,23,3,404]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minJumps([7]), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.minJumps([7,6,9,6,9,6,9,7]), 1)

if __name__ == '__main__':
    unittest.main()
