import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxDistance([1,1,1,6,1,1,1]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maxDistance([1,8,3,8,3]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.maxDistance([0,1]), 1)

if __name__ == '__main__':
    unittest.main()
