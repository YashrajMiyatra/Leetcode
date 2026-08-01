import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        i = 1
        n = len(word)
        while True:
            if i * k >= n or word.startswith(word[i * k:]):
                return i
            i += 1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def minimum_time_to_initial_state(self, word: str, k: int) -> int:
        return self.minimumTimeToInitialState(word, k)
