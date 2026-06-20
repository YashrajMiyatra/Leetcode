import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.eatenApples([1,2,3,5,2], [3,2,1,4,2]), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.eatenApples([3,0,0,0,0,2], [3,0,0,0,0,2]), 5)

if __name__ == '__main__':
    unittest.main()
