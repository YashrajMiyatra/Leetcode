import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumCost("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5]), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.minimumCost("aaaa", ["z","zz","zzz"], [1,10,100]), -1)

if __name__ == '__main__':
    unittest.main()
