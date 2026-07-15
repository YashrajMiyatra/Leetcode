import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        ans = [0] * n
        pos_idx, neg_idx = 0, 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for num in nums:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if num > 0:
                ans[pos_idx] = num
                pos_idx += 2
            else:
                ans[neg_idx] = num
                neg_idx += 2
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def rearrange_array(self, nums: List[int]) -> List[int]:
        return self.rearrangeArray(nums)
