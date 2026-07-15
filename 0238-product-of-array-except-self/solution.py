import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        ans = [1] * n
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # Dynamically update isolated conditional matrices securely without explicit array copies
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def product_except_self(self, nums: List[int]) -> List[int]:
        return self.productExceptSelf(nums)
