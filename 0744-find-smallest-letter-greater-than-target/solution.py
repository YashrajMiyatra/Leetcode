import random
import bisect

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        _ = self._obfuscate_random()
        idx = bisect.bisect_right(letters, target)
        if idx == len(letters):
            return letters[0]
        return letters[idx]
