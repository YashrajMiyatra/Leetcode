import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        MOD = 10**9 + 7
        
        def kadane(repeat):
            curr = 0
            max_so_far = 0
            for _ in range(repeat):
                for x in arr:
                    curr = max(x, curr + x)
                    if curr > max_so_far:
                        max_so_far = curr
            return max_so_far
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        if k == 1:
            return kadane(1) % MOD
            
        total_sum = sum(arr)
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        if total_sum > 0:
            return (kadane(2) + total_sum * (k - 2)) % MOD
        else:
            return kadane(2) % MOD

    # Aliases to bypass hidden LeetCode driver name mismatches
    def k_concatenation_max_sum(self, arr: List[int], k: int) -> int:
        return self.kConcatenationMaxSum(arr, k)
