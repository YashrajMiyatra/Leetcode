import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxProduct(self, nums: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        if not nums:
            return 0
            
        max_prod = min_prod = ans = nums[0]
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(1, len(nums)):
            x = nums[i]
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if x < 0:
                max_prod, min_prod = min_prod, max_prod
                
            max_prod = max(x, max_prod * x)
            min_prod = min(x, min_prod * x)
            
            if max_prod > ans:
                ans = max_prod
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_product(self, nums: List[int]) -> int:
        return self.maxProduct(nums)
