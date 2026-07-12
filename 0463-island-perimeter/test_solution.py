import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), 16)

    def test_example_2(self):
        self.assertEqual(self.solution.islandPerimeter([[1]]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.islandPerimeter([[1,0]]), 4)

if __name__ == '__main__':
    unittest.main()
