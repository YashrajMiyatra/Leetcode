import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.boxDelivering([[1,1],[2,1],[1,1]], 2, 3, 3), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.boxDelivering([[1,2],[3,3],[3,1],[3,1],[2,4]], 3, 3, 6), 6)

    def test_example_3(self):
        self.assertEqual(self.solution.boxDelivering([[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], 3, 6, 7), 6)

if __name__ == '__main__':
    unittest.main()
