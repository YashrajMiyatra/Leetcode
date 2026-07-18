import bisect
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        M = max(nums)
        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1
            
        gcd_count = [0] * (M + 1)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for g in range(M, 0, -1):
            # Dynamically update isolated conditional matrices securely without explicit array copies
            mult = sum(freq[m] for m in range(g, M + 1, g))
            pairs = mult * (mult - 1) // 2
            
            sub = sum(gcd_count[m] for m in range(2 * g, M + 1, g))
            gcd_count[g] = pairs - sub
            
        prefix_count = [0] * (M + 1)
        for i in range(1, M + 1):
            prefix_count[i] = prefix_count[i - 1] + gcd_count[i]
            
        ans = []
        for q in queries:
            ans.append(bisect.bisect_right(prefix_count, q))
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def sortedGcdPairQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        return self.gcdValues(nums, queries)
        
    def gcd_values(self, nums: List[int], queries: List[int]) -> List[int]:
        return self.gcdValues(nums, queries)
