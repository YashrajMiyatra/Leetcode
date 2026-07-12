import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumDistance([1,2,1,1,3]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumDistance([1,1,2,3,2,1,2]), 8)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumDistance([1]), -1)

if __name__ == '__main__':
    unittest.main()
