import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        res = self.solution.readBinaryWatch(1)
        expected = ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        self.assertCountEqual(res, expected)

    def test_example_2(self):
        self.assertEqual(self.solution.readBinaryWatch(9), [])

if __name__ == '__main__':
    unittest.main()
