import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        wordsContainer = ["abcd","bcd","xbcd"]
        wordsQuery = ["cd","bcd","xyz"]
        expected = [1, 1, 1]
        self.assertEqual(self.sol.stringIndices(wordsContainer, wordsQuery), expected)

    def test_example2(self):
        wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
        wordsQuery = ["gh","acbfgh","acbfegh"]
        expected = [2, 0, 2]
        self.assertEqual(self.sol.stringIndices(wordsContainer, wordsQuery), expected)

    def test_no_common_suffix(self):
        wordsContainer = ["a", "b", "c"]
        wordsQuery = ["x", "y", "z"]
        # Empty suffix matches all. Tie breaks: smallest length (all length 1), 
        # then earliest index -> index 0.
        expected = [0, 0, 0]
        self.assertEqual(self.sol.stringIndices(wordsContainer, wordsQuery), expected)

    def test_exact_match(self):
        wordsContainer = ["hello", "world"]
        wordsQuery = ["hello", "world", "llo"]
        # "llo" matches "hello"
        expected = [0, 1, 0]
        self.assertEqual(self.sol.stringIndices(wordsContainer, wordsQuery), expected)
        
    def test_tie_breaking_length(self):
        wordsContainer = ["xabc", "abc", "xxabc"]
        wordsQuery = ["yabc"]
        # all have suffix "abc", shortest is "abc" at index 1
        expected = [1]
        self.assertEqual(self.sol.stringIndices(wordsContainer, wordsQuery), expected)

if __name__ == '__main__':
    unittest.main()
