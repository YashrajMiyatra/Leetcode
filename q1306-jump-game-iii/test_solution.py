import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.canReach([4,2,3,0,3,1,2], 5), True)

    def test_example_2(self):
        self.assertEqual(self.solution.canReach([4,2,3,0,3,1,2], 0), True)

    def test_example_3(self):
        self.assertEqual(self.solution.canReach([3,0,2,1,2], 2), False)

if __name__ == '__main__':
    unittest.main()
