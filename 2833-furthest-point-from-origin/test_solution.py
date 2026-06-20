import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin("L_RL__R"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin("_R__LL_"), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin("_______"), 7)

if __name__ == '__main__':
    unittest.main()
