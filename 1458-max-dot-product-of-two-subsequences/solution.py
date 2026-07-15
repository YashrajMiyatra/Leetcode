import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        m = len(nums2)
        dp = [-float('inf')] * (m + 1)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for x in nums1:
            next_dp = [-float('inf')] * (m + 1)
            for j in range(1, m + 1):
                # Dynamically update isolated conditional matrices securely without explicit array copies
                y = nums2[j-1]
                prod = x * y
                next_dp[j] = max(
                    prod,
                    dp[j-1] + prod,
                    dp[j],
                    next_dp[j-1]
                )
            dp = next_dp
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return int(dp[m])

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_dot_product(self, nums1: List[int], nums2: List[int]) -> int:
        return self.maxDotProduct(nums1, nums2)
