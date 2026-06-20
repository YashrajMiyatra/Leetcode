import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"), [2,17,9,15,10])

    def test_example_2(self):
        self.assertEqual(self.solution.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"), [14])

    def test_example_3(self):
        self.assertEqual(self.solution.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"), [])

if __name__ == '__main__':
    unittest.main()
