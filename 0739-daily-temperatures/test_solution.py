import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])

    def test_example_2(self):
        self.assertEqual(self.solution.dailyTemperatures([30,40,50,60]), [1,1,1,0])

    def test_example_3(self):
        self.assertEqual(self.solution.dailyTemperatures([30,60,90]), [1,1,0])

if __name__ == '__main__':
    unittest.main()
