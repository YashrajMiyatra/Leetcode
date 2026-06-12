import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumRemovals([2,1,5], 2), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumRemovals([1,6,2,9], 3), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumRemovals([4,6], 2), 0)

if __name__ == '__main__':
    unittest.main()
