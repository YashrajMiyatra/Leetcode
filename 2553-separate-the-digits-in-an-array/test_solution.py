import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.separateDigits([13,25,83,77]), [1,3,2,5,8,3,7,7])

    def test_example_2(self):
        self.assertEqual(self.solution.separateDigits([7,1,3,9]), [7,1,3,9])

if __name__ == '__main__':
    unittest.main()
