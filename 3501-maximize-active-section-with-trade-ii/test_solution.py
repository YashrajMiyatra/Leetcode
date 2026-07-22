import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximizeActiveSection("01", [[0,1]]), [1])

    def test_example_2(self):
        self.assertEqual(self.solution.maximizeActiveSection("0100", [[0,3],[0,2],[1,3],[2,3]]), [4,3,1,1])

    def test_example_3(self):
        self.assertEqual(self.solution.maximizeActiveSection("1000100", [[1,5],[0,6],[0,4]]), [6,7,2])

    def test_example_4(self):
        self.assertEqual(self.solution.maximizeActiveSection("01010", [[0,3],[1,4],[1,3]]), [4,4,2])

if __name__ == '__main__':
    unittest.main()
