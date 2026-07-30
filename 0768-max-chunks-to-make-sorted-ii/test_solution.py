import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxChunksToSorted([5,4,3,2,1]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maxChunksToSorted([2,1,3,4,4]), 4)

if __name__ == '__main__':
    unittest.main()
