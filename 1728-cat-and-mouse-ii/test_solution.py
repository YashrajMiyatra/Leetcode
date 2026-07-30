import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.canMouseWin(["####F","#C...","M...."], 1, 2))

    def test_example_2(self):
        self.assertTrue(self.solution.canMouseWin(["M.C...F"], 1, 4))

    def test_example_3(self):
        self.assertFalse(self.solution.canMouseWin(["M.C...F"], 1, 3))

if __name__ == '__main__':
    unittest.main()
