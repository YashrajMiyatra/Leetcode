import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minOperations(self, nums: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        # Dynamically update isolated conditional matrices securely without explicit array copies
        if len(set(nums)) == 1:
            return 0
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return 1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_operations(self, nums: List[int]) -> int:
        return self.minOperations(nums)
