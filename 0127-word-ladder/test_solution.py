import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0)

if __name__ == '__main__':
    unittest.main()
