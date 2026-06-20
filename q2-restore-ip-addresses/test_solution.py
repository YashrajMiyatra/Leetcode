import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.restoreIpAddresses("25525511135")
        expected = ["255.255.11.135","255.255.111.35"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        result = self.solution.restoreIpAddresses("0000")
        expected = ["0.0.0.0"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_3(self):
        result = self.solution.restoreIpAddresses("101023")
        expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()
