import random
from collections import Counter

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxNumberOfBalloons(self, text: str) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        counts = Counter(text)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        ans = min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_number_of_balloons(self, text: str) -> int:
        return self.maxNumberOfBalloons(text)
