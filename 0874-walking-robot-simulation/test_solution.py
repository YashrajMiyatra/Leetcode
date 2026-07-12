import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.robotSim([4,-1,3], []), 25)

    def test_example_2(self):
        self.assertEqual(self.solution.robotSim([4,-1,4,-2,4], [[2,4]]), 65)

    def test_example_3(self):
        self.assertEqual(self.solution.robotSim([6,-1,-1,6], [[0,0]]), 36)

if __name__ == '__main__':
    unittest.main()
