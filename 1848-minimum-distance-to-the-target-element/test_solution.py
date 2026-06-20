import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.getMinDistance([1,2,3,4,5], 5, 3), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.getMinDistance([1], 1, 0), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 0), 0)

if __name__ == '__main__':
    unittest.main()
