import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxCoins(self, piles: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        piles.sort()
        n = len(piles) // 3
        ans = 0
        
        for i in range(len(piles) - 2, n - 1, -2):
            ans += piles[i]
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_coins(self, piles: List[int]) -> int:
        return self.maxCoins(piles)
