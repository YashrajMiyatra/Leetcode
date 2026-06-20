import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.constructProductMatrix([[1,2],[3,4]]), [[24,12],[8,6]])

    def test_example_2(self):
        self.assertEqual(self.solution.constructProductMatrix([[12345],[2],[1]]), [[2],[0],[0]])

if __name__ == '__main__':
    unittest.main()
