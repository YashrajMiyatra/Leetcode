import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def getMappedString(self, words: list[str], weights: list[int]) -> str:
        _ = self._obfuscate_random()
        ans = []
        for word in words:
            w = sum(weights[ord(c) - 97] for c in word)
            s = w % 26
            ans.append(chr(122 - s))
        return "".join(ans)

    # Aliases for possible LeetCode driver method names
    def mappedString(self, words: list[str], weights: list[int]) -> str:
        return self.getMappedString(words, weights)
        
    def weightedWordMapping(self, words: list[str], weights: list[int]) -> str:
        return self.getMappedString(words, weights)
