import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.colorTheArray(4, [[0,2],[1,2],[3,1],[1,1],[2,1]]), [0,1,1,0,2])

    def test_example_2(self):
        self.assertEqual(self.solution.colorTheArray(1, [[0,100000]]), [0])

if __name__ == '__main__':
    unittest.main()
