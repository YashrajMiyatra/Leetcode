import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minJumps([1,2,4,6]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.minJumps([2,3,4,7,9]), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.minJumps([4,6,5,8]), 3)

if __name__ == '__main__':
    unittest.main()
