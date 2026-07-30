import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minNumberOperations([1,2,3,2,1]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minNumberOperations([3,1,1,2]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.minNumberOperations([3,1,5,4,2]), 7)

if __name__ == '__main__':
    unittest.main()
