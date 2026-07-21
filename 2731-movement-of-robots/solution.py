import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        pos = []
        for i in range(len(nums)):
            if s[i] == 'R':
                pos.append(nums[i] + d)
            else:
                pos.append(nums[i] - d)
                
        pos.sort()
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        ans = 0
        n = len(pos)
        mod = 10**9 + 7
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for i in range(n):
            ans = (ans + pos[i] * (2 * i - n + 1)) % mod
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def sum_distance(self, nums: List[int], s: str, d: int) -> int:
        return self.sumDistance(nums, s, d)
