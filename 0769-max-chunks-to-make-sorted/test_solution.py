import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxChunksToSorted([4,3,2,1,0]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.maxChunksToSorted([1,0,2,3,4]), 4)

if __name__ == '__main__':
    unittest.main()
