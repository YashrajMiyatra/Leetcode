import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kthLargestValue([[5,2],[1,6]], 1), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.kthLargestValue([[5,2],[1,6]], 2), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.kthLargestValue([[5,2],[1,6]], 3), 4)

if __name__ == '__main__':
    unittest.main()
