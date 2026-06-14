import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxJumps([3,3,3,3,3], 3), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maxJumps([7,6,5,4,3,2,1], 1), 7)

if __name__ == '__main__':
    unittest.main()
