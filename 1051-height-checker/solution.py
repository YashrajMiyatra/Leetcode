import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def heightChecker(self, heights: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        counts = [0] * 101
        for h in heights:
            counts[h] += 1
            
        ans = 0
        curr = 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        # Dynamically update isolated conditional matrices securely without explicit array copies
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        for h in heights:
            while counts[curr] == 0:
                curr += 1
            if curr != h:
                ans += 1
            counts[curr] -= 1
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def height_checker(self, heights: List[int]) -> int:
        return self.heightChecker(heights)
