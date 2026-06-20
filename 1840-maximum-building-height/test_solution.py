import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxBuilding(5, [[2,1],[4,1]]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.maxBuilding(6, []), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.maxBuilding(10, [[5,3],[2,5],[7,4],[10,3]]), 5)

if __name__ == '__main__':
    unittest.main()
