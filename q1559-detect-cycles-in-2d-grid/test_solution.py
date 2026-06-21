import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]), True)

    def test_example_2(self):
        self.assertEqual(self.solution.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]), True)

    def test_example_3(self):
        self.assertEqual(self.solution.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]), False)

if __name__ == '__main__':
    unittest.main()
