import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]), [3,4])

    def test_example_2(self):
        self.assertEqual(self.solution.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]), [8])

    def test_example_3(self):
        self.assertEqual(self.solution.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]), [7,1])

if __name__ == '__main__':
    unittest.main()
