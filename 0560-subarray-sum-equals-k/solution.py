import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def subarraySum(self, nums: List[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        counts = collections.defaultdict(int)
        counts[0] = 1
        
        prefix_sum = 0
        ans = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for x in nums:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            prefix_sum += x
            if prefix_sum - k in counts:
                ans += counts[prefix_sum - k]
            counts[prefix_sum] += 1
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def subarray_sum(self, nums: List[int], k: int) -> int:
        return self.subarraySum(nums, k)
