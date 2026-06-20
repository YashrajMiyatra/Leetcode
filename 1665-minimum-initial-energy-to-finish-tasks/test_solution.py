import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumEffort([[1,2],[2,4],[4,8]]), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]]), 32)

    def test_example_3(self):
        self.assertEqual(self.solution.minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]), 27)

if __name__ == '__main__':
    unittest.main()
