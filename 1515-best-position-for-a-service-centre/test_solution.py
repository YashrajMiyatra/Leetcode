import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        positions = [[0,1],[1,0],[1,2],[2,1]]
        result = s.getMinDistSum(positions)
        self.assertAlmostEqual(result, 4.00000, places=5)

    def test_example2(self):
        s = Solution()
        positions = [[1,1],[3,3]]
        result = s.getMinDistSum(positions)
        self.assertAlmostEqual(result, 2.82843, places=5)
        
    def test_single_point(self):
        s = Solution()
        positions = [[50, 50]]
        result = s.getMinDistSum(positions)
        self.assertAlmostEqual(result, 0.00000, places=5)

if __name__ == '__main__':
    unittest.main()
