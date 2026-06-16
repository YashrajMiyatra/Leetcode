import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.plusOne([1,2,3]), [1,2,4])

    def test_example_2(self):
        self.assertEqual(self.solution.plusOne([4,3,2,1]), [4,3,2,2])

    def test_example_3(self):
        self.assertEqual(self.solution.plusOne([9]), [1,0])

if __name__ == '__main__':
    unittest.main()
