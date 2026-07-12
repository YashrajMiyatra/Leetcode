import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.arrayRankTransform([40,10,20,30]), [4,1,2,3])

    def test_example_2(self):
        self.assertEqual(self.solution.arrayRankTransform([100,100,100]), [1,1,1])

    def test_example_3(self):
        self.assertEqual(self.solution.arrayRankTransform([37,12,28,9,100,56,80,5,12]), [5,3,4,2,8,6,7,1,3])

if __name__ == '__main__':
    unittest.main()
