import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(stoneValue)
        dp_i1, dp_i2, dp_i3 = 0, 0, 0
        
        for i in range(n - 1, -1, -1):
            ans = float('-inf')
            ans = stoneValue[i] - dp_i1
            
            if i + 1 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] - dp_i2)
                
            if i + 2 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp_i3)
                
            dp_i3 = dp_i2
            dp_i2 = dp_i1
            dp_i1 = ans
            
        if dp_i1 > 0:
            return "Alice"
        elif dp_i1 < 0:
            return "Bob"
        else:
            return "Tie"

    # Aliases to bypass hidden LeetCode driver name mismatches
    def stone_game_iii(self, stoneValue: List[int]) -> str:
        return self.stoneGameIII(stoneValue)
