import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.search([-1,0,3,5,9,12], 9), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.search([-1,0,3,5,9,12], 2), -1)

if __name__ == '__main__':
    unittest.main()
