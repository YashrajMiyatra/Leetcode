import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        count = [0]*256
        count[1] = 1; count[2] = 3; count[3] = 4
        ans = self.solution.sampleStats(count)
        self.assertAlmostEqual(ans[0], 1.0, places=5)
        self.assertAlmostEqual(ans[1], 3.0, places=5)
        self.assertAlmostEqual(ans[2], 2.375, places=5)
        self.assertAlmostEqual(ans[3], 2.5, places=5)
        self.assertAlmostEqual(ans[4], 3.0, places=5)

if __name__ == '__main__':
    unittest.main()
