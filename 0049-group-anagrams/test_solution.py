import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        res = self.solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        res = [sorted(g) for g in res]
        res.sort()
        expected = [sorted(["bat"]), sorted(["nat","tan"]), sorted(["ate","eat","tea"])]
        expected.sort()
        self.assertEqual(res, expected)

    def test_example_2(self):
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])

    def test_example_3(self):
        self.assertEqual(self.solution.groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()
