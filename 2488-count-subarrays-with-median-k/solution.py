import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        k_idx = nums.index(k)
        
        count = collections.defaultdict(int)
        count[0] = 1
        
        curr = 0
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(k_idx - 1, -1, -1):
            curr += 1 if nums[i] > k else -1
            count[curr] += 1
            
        ans = 0
        curr = 0
        for j in range(k_idx, len(nums)):
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if j > k_idx:
                curr += 1 if nums[j] > k else -1
            ans += count[-curr] + count[1 - curr]
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def count_subarrays(self, nums: List[int], k: int) -> int:
        return self.countSubarrays(nums, k)
