import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.sortArray([5,2,3,1]), [1,2,3,5])

    def test_example_2(self):
        self.assertEqual(self.solution.sortArray([5,1,1,2,0,0]), [0,0,1,1,2,5])

if __name__ == '__main__':
    unittest.main()
