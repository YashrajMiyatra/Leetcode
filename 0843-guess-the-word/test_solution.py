import unittest
from solution import Solution

class Master:
    def __init__(self, secret, words):
        self.secret = secret
        self.words = set(words)
        self.guesses = 0
        
    def guess(self, word: str) -> int:
        self.guesses += 1
        if word not in self.words:
            return -1
        return sum(c1 == c2 for c1, c2 in zip(word, self.secret))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        words = ["acckzz","ccbazz","eiowzz","abcczz"]
        secret = "acckzz"
        master = Master(secret, words)
        self.solution.findSecretWord(words, master)
        self.assertLessEqual(master.guesses, 10)

    def test_example_2(self):
        words = ["hamada","khaled"]
        secret = "hamada"
        master = Master(secret, words)
        self.solution.findSecretWord(words, master)
        self.assertLessEqual(master.guesses, 10)

if __name__ == '__main__':
    unittest.main()
