import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([8,1,2,2,3]), [4,0,1,1,3])

    def test_example_2(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([6,5,4,8]), [2,1,0,3])

    def test_example_3(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([7,7,7,7]), [0,0,0,0])

if __name__ == '__main__':
    unittest.main()
