import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.sortByBits([0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])

    def test_example_2(self):
        self.assertEqual(self.solution.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])

if __name__ == '__main__':
    unittest.main()
